import config
import threading
import requests
import telebot
from telebot import types
import time

url_1 = "https://greenhub.kz/api/v1/get-notifications"
url_2 = "https://greenhub.kz/api/v1/login"
url_3 = "https://greenhub.kz/api/v1/create-application"


# A - authorized user
# N - not authorized user


bot = telebot.TeleBot(config.token)
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(*[types.KeyboardButton(name) for name in ["Авторизоваться", "Заказать услугу", "Информация"]])

auth_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
auth_keyboard.add(*[types.KeyboardButton(name) for name in ["Выйти из аккаунта", "Заказать услугу", "Информация"]])


@bot.message_handler(commands=['start'])
def start(message):
    print('User ' + str(message.chat.id) + ' is connected')
    print(message)
    print('__________________________________')
    # bot.send_message(message.chat.id, "Приветсвуем в боте", reply_markup=keyboard)
    # bot.send_message(message.chat.id, "Убираем клавиатуру", reply_markup=types.ReplyKeyboardRemove())
    main_menu(message, 'N')


def main_menu(message, auth_status):
    if auth_status == 'A':
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=auth_keyboard)
        bot.register_next_step_handler(message, menu_user_choice, 'A')
    else:
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=keyboard)
        bot.register_next_step_handler(message, menu_user_choice, 'N')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    additions_inline_buttons = types.InlineKeyboardMarkup()

    if call.data == "Кнопка 1":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 1.1", "Услуга 1.2", "Услуга 1.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 2":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 2.1", "Услуга 2.2", "Услуга 2.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 3":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 3.1", "Услуга 3.2", "Услуга 3.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 4":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 4.1", "Услуга 4.2", "Услуга 4.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 5":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 5.1", "Услуга 5.2", "Услуга 5.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 6":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 6.1", "Услуга 6.2", "Услуга 6.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 7":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 7.1", "Услуга 7.2", "Услуга 7.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 8":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 8.1", "Услуга 8.2", "Услуга 8.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    elif call.data == "Кнопка 9":
        additions_inline_buttons.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                                       ["Услуга 9.1", "Услуга 9.2", "Услуга 9.3"]])
        bot.send_message(call.message.chat.id, "Выберите услугу:", reply_markup=additions_inline_buttons)

    else:

        json = {
          "chatId": call.message.chat.id,
          "serviceId": call.data
          # ,"phone": message.contact.phone_number
        }

        r = requests.post(url_3, json=json)
        response = r.json()

        if response['error'] == 'Phone required':
            keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
            keyboard_2.add(button_phone)
            bot.send_message(call.message.chat.id, "Отправьте нам ваш номер телефона (нажать на кнопку)",
                             reply_markup=keyboard_2)
            bot.register_next_step_handler(call.message, order_to_server, call.data)

        else:
            bot.send_message(call.message.chat.id, "Спасибо, ваша заявка на услугу " + str(call.data) +
                             " успешно отправлена")
        main_menu(call.message)


def menu_user_choice(message, auth_status):
    if auth_status == 'A':
        if message.text == "Выйти из аккаунта":
            authorization(message)
        elif message.text == "Заказать услугу":
            do_order(message, 'A')
        elif message.text == "Информация":
            about_information(message, 'A')
        elif message.text == "/start":
            main_menu(message, 'A')
        else:
            bot.send_message(message.chat.id, "Неправильная команда")
            main_menu(message, 'A')
    else:
        if message.text == "Авторизоваться":
            authorization(message)
        elif message.text == "Заказать услугу":
            do_order(message, 'N')
        elif message.text == "Информация":
            about_information(message, 'N')
        elif message.text == "/start":
            main_menu(message, 'N')
        else:
            bot.send_message(message.chat.id, "Неправильная команда")
            main_menu(message, 'N')


def about_information(message, auth_status):
    bot.send_message(message.chat.id, "Описание деятельности компании")

    if auth_status == 'A':
        main_menu(message, 'A')
    else:
        main_menu(message, 'N')


def authorization(message):
    bot.send_message(message.chat.id, "Введите логин")
    bot.register_next_step_handler(message, authorization_2_step)


def authorization_2_step(message):
    login = message.text
    bot.send_message(message.chat.id, "Введите пароль")
    bot.register_next_step_handler(message, authorization_3_step, login)


def authorization_3_step(message, login):
    password = message.text
    chat_id = message.chat.id
    json = {
        "login": login,
        "password": password,
        "chatId": chat_id
    }

    r = requests.post(url_2, json=json)
    print(r.json())
    print(r.status_code)
    response = r.json()

    if response['error'] == None:
        bot.send_message(message.chat.id, 'Вы успешно вошли как ' + login)
        main_menu(message, 'A')
    else:
        bot.send_message(message.chat.id, 'Неправильный логин или пароль')
        main_menu(message, 'N')


def do_order(message):
    inline_buttons_order = types.InlineKeyboardMarkup()
    inline_buttons_order.add(*[types.InlineKeyboardButton(name, callback_data=name) for name in
                               ["Кнопка 1", "Кнопка 2", "Кнопка 3", "Кнопка 4", "Кнопка 5", "Кнопка 6", "Кнопка 7",
                                "Кнопка 8", "Кнопка 9"]])
    bot.send_message(message.chat.id, "Выберите тип услуги:", reply_markup=inline_buttons_order)


def order_to_server(message, serviceId):

    json = {
      "chatId": message.chat.id,
      "serviceId": serviceId,
      "phone": message.contact.phone_number
    }

    r = requests.post(url_3, json=json)
    print(r.json())
    bot.send_message(message.chat.id, "Спасибо, ваша заявка успешно отправлена")
    main_menu(message)


# Отдельный поток отвечающий за рассылку уведомлений
def notification(interval):
    while True:
        r = requests.get(url_1)
        response = r.json()
        print(response)
        for i in response:
            bot.send_message(int(i['chatId']), i['text'])
        time.sleep(interval)


t = threading.Thread(target=notification, args=(10,))
t.daemon = True
t.start()

if __name__ == '__main__':
    bot.polling(none_stop=True)
