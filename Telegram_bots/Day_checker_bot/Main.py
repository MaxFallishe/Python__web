import telebot
from telebot import types
from datetime import datetime
import threading
import sqlite3
import time
import pytz


bot = telebot.TeleBot("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
admin_id = 562036772  # 410680216 - Максима
database = "DayChecker_DB.db"

listAknietWorkStart = [734229885, "08:45", "08:45", "08:45", "08:45", "08:45"]
listArtemWorkStart = [395585922, "10:15", "08:45", "10:15", "08:45", "10:15"]
listDianaWorkStart = [428954941, "08:45", "08:45", "08:45", "08:45", "08:45"]
listNikitaWorkStart = [562036772, "07:30", "07:30", "07:30", "07:30", "07:30"]
listLenkorsWorkStart = [705090811, "10:15", "10:15", "10:15", "10:15", "10:15"]
listAlisherWorkStart = [480642428, "10:15", "10:15", "10:15", "10:15", "10:15"]
listSashaWorkStart = [241901437, "10:15", "10:15", "10:15", "10:15", "10:15"]
listMaksimWorkStart = [410680216, "09:45", "09:45", "09:45", "09:45", "09:45"]
listIlyaWorkStart = [201941791, "08:45", "08:45", "08:45", "08:45", "08:45"]

listEmployeesWorkStart = [listAknietWorkStart, listArtemWorkStart, listDianaWorkStart, listNikitaWorkStart,
                          listLenkorsWorkStart, listAlisherWorkStart, listSashaWorkStart, listMaksimWorkStart,
                          listIlyaWorkStart]

listAknietWorkEnd = [734229885, "18:30", "18:30", "18:30", "18:30", "18:30"]  # узнал
listArtemWorkEnd = [395585922, "20:15", "20:15", "20:15", "20:15", "20:15"]  # узнал
listDianaWorkEnd = [428954941, "18:30", "18:30", "18:30", "18:30", "18:30"]  # узнал
listNikitaWorkEnd = [562036772, "21:00", "21:00", "21:00", "21:00", "21:00"]  # узнал
listLenkorsWorkEnd = [705090811, "19:10", "19:10", "19:10", "19:10", "19:10"]  # узнал
listAlisherWorkEnd = [480642428, "20:30", "20:30", "20:30", "20:30", "20:30"]  # узнал
listSashaWorkEnd = [241901437, "19:45", "19:45", "19:45", "19:45", "19:45"]   # узнал
listMaksimWorkEnd = [410680216, "21:45", "21:45", "21:45", "21:45", "21:45"]  # узнал
listIlyaWorkEnd = [201941791, "08:45", "08:45", "08:45", "08:45", "08:45"]  #

listEmployeesWorkEnd = [listAknietWorkEnd, listArtemWorkEnd, listDianaWorkEnd, listNikitaWorkEnd,
                        listLenkorsWorkEnd, listAlisherWorkEnd, listSashaWorkEnd, listMaksimWorkEnd,
                        listIlyaWorkEnd]


reported = []
marked = []

reportTime = "18:00"


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == "Отметиться":
        geolocation(message)
    elif message.text == "Отправить отчёт":
        report_load(message)
    elif message.text == "/start":
        start(message)
    else:
        bot.send_message(message.chat.id, "Такой команды не существует")


# ##### General Code ##### #
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Вас приветствует бот SailetDay")
    main_menu(message)


def main_menu(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ["Отметиться", "Отправить отчёт"]])
        bot.send_message(message.chat.id,
                         "Вы в главном меню \nВнимание, учтите что отметиться и отправить отчёт можно только раз в день", reply_markup=keyboard)
        bot.register_next_step_handler(message, check_start)
        print("User ", message.chat.id, "wrote /start")
    except Exception as e:
        print("Error", e)
        bot.send_message(message.chat.id, "Что-то пошло не так... Повторите попытку")
        start(message)


def check_start(message):
    if message.text == "Отметиться":
        geolocation(message)
    elif message.text == "Отправить отчёт":
        report_load(message)
    else:
        bot.send_message(message.chat.id, "Такой команды не существует")
        main_menu(message)


def geolocation(message):
    if message.chat.id in marked:
        bot.send_message(message.chat.id, "Сегодня вы уже отмечались")
        main_menu(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "Для начала отправьте своё местоположение нажав на кнопку", reply_markup=keyboard)
        bot.register_next_step_handler(message, check)


def check(message):
    try:
        print(message.location.latitude, message.location.longitude)
        bot.send_message(message.chat.id, "Отправьте фото с места работы(именно как фото, а не как файл)", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, repeat, message.location.latitude, message.location.longitude)
    except Exception as e:
        print("Error", e)
        bot.send_message(message.chat.id, "Что-то пошло не так... Повторите попытку")
        main_menu(message)


def repeat(message, latitude, longitude):
    try:
        now_weekday = str(datetime.now(pytz.timezone('Asia/Almaty')).weekday() + 1)
        now_data_time = str(datetime.now(pytz.timezone('Asia/Almaty')).strftime('%Y-%m-%d %H:%M:%S'))

        print("Отправлено фото с id: ", message.photo[0].file_id, ", Фото отправил: ", message.from_user.first_name,
              ", Время отправления: ", now_data_time)

        status = '1'  # В будущем будет отображать своемременность отметки
        geo = str(latitude) + " " + str(longitude)
        report_attributes = (str(message.chat.id), str(message.from_user.username), now_weekday, now_data_time, status, geo)

        bot.send_message(admin_id, "Фото от " + str(message.from_user.first_name) + "\n" + now_data_time)
        bot.send_photo(admin_id, message.photo[0].file_id)
        bot.send_location(admin_id, latitude, longitude)

        db_write_mark(database, report_attributes)
        bot.send_message(message.chat.id, "Вы отметились")
        marked.append(message.chat.id)
        print(marked)
        main_menu(message)

    except Exception as e:
        print("Error", e)
        bot.send_message(message.chat.id, "Что-то пошло не так... Повторите попытку")
        main_menu(message)

def report_load(message):  # добавить try
    if message.chat.id in reported:
        bot.send_message(message.chat.id, "Сегодня вы уже отправляли отчёт")
        main_menu(message)
    else:
        try:
            bot.send_message(message.chat.id, "Сделай Ctrl+C твоего отчёта и вставь его в сообщение ", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, report_send)

        except Exception as e:
            print("Error", e)
            bot.send_message(message.chat.id, "Что-то пошло не так... Повторите попытку")
            main_menu(message)


def report_send(message):  # добавить try
    try:

        now_weekday = str(datetime.now(pytz.timezone('Asia/Almaty')).weekday() + 1)
        now_data_time = str(datetime.now(pytz.timezone('Asia/Almaty')).strftime('%Y-%m-%d %H:%M:%S'))
        bot.send_message(admin_id, "Отчёт от " + str(message.from_user.first_name) + "\n" + now_data_time + "\n"
                         + message.text)

        status = '1'  # В будущем будет отображать своемременность отметки

        report_attributes = (str(message.chat.id), str(message.from_user.username), now_weekday, now_data_time, status, message.text)

        db_write_report(database, report_attributes)

        bot.send_message(message.chat.id, "Отчёт успешно отправлен")

        reported.append(message.chat.id)
        print(reported)

        main_menu(message)

    except Exception as e:
        print("Error", e)
        bot.send_message(message.chat.id, "Что-то пошло не так... Повторите попытку")
        main_menu(message)


def db_write_report(db_name, inserting_values):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Reports VALUES (NULL, ?, ?, ?, ?, ?, ? )", inserting_values)
    conn.commit()
    conn.close()


def db_write_mark(db_name, inserting_values):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Morning_checks VALUES (NULL, ?, ?, ?, ?, ?, ? )", inserting_values)
    conn.commit()
    conn.close()

# Отдельный поток отвечающий за рассылку уведомлений
def notifications(interval):
    while True:

        kz_time_obj = datetime.now(pytz.timezone('Asia/Almaty'))
        today_day = kz_time_obj.weekday()
        time_now = kz_time_obj.strftime('%H:%M')

        if today_day+1 == 6 or today_day+1 == 7:  # 0 - monday, than do +1
            print(kz_time_obj.strftime('%H:%M'))  # Время  в часах и минутах  (str)
            print(kz_time_obj.weekday() + 1)  # День недели в цифровом значении  (int)
            print("Yes, today free day")

        else:
            print(kz_time_obj.strftime('%H:%M'))  # Время  в часах и минутах  (str)
            print(kz_time_obj.weekday() + 1)  # День недели в цифровом значении  (int)

            for i in listEmployeesWorkStart:
                if i[today_day + 1] == time_now:
                    bot.send_message(i[0], "Это напоминалка,\nНе забудь отметиться")

            for i in listEmployeesWorkEnd:
                if i[today_day + 1] == time_now:
                    bot.send_message(i[0], "Это напоминалка,\nНе забудь отправить отчёт")

        time.sleep(interval)


t = threading.Thread(target=notifications, args=(60,))
t.daemon = True
t.start()


if __name__ == '__main__':
    bot.polling(none_stop=True)
