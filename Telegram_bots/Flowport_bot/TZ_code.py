import config
import requests
import telebot
import json
from telebot import apihelper
from telebot import types
import sqlite3
import logging
import os
#ip = '182.16.14.245'
#port = '1080'

#apihelper.proxy = {
#  'https': 'socks5://{}:{}'.format(ip,port)
#}


#oper_with_db("UPDATE text_for_user SET text='Это измененный текст' WHERE id=12")    -
#    допилить апдейт для админки обязательно исползовать условие WHERE иначе на данный текст будет заменен весь столбец

# buttons = types.InlineKeyBoardMarkup() - Создание Inline кнопку
# buttons.add(*[types.InlineKeyboardButton(name,callback_data = name) for name in ["Да","Нет"]]) - 'Доп. инф.  в группе


#button.add(types)           -



bot = telebot.TeleBot(config.token)

_db_Number_of_User = 0

_db_User_Status = 0

Favorites = ""
myArray =[_db_Number_of_User,_db_User_Status]
OnefromFavorites = ""

WaitMode = 0
UserMode = 1
AdminMode = 2

logging.info('The main program variables are declared')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log')



#logging.debug('A debug message')
#logging.info('Some information')
#logging.warning('A shot across the bows')








@bot.message_handler(commands = ['start'])
def start(message):
    global UserID



    print("user inside")


    UserID = message.from_user.id   #используются для работы с инлайн кнопками

    try:
        res = cursorConnectionAndRead("SELECT Status FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)
        res =int(res[0][0])

        if res == 1:
            logging.info('The user started working as "user"')
            userRights(message)
        elif res == 0:
            considiration(message)
        elif res ==2:
            logging.info('The user started working as "admin"')
            adminRights(message)

    except:
        main(message)


@bot.message_handler(commands =['info'])
def info(message):
    logging.info('The user sent a request for their status')
    try:
        res = cursorConnectionAndRead(
            "SELECT Status FROM First_4_answers WHERE UserTelegrammID =%s" % message.from_user.id)
        res = int(res[0][0])
        print(res)
        if res == 0:
            bot.send_message(message.chat.id,
                             'Ваша заявка ещё на рассмотрении администратора,Ожидайте ')
        elif res == 1:
            bot.send_message(message.chat.id,
                             'Вы зарегестрированы как "Пользователь", отправьте команду /start для начала работы с ботом')
        elif res == 2:
            bot.send_message(message.chat.id,
                             'Вы зарегестрированы как "Админ", отправьте команду /start для начала работы с ботом')

    except:
        bot.send_message(message.chat.id,'Пока вы не зарегисрированы, отправьте  команду /start для регистрации')
    logging.info('The user has received information about his status')







@bot.message_handler(commands = ['admin'])
def adminModeActivation(message):
    logging.info('user attempt to get admin rights')
    bot.send_message(message.chat.id,"Вы ввели команду для получения прав Админа ")
    bot.send_message(message.chat.id,"Введите пароль:")
    bot.register_next_step_handler(message,adminPasswordCheck)



def main(message):
    global results
    global myArray

    myArray = list(myArray)
    myArray = [_db_Number_of_User, _db_User_Status]



    results = cursorConnectionAndRead("SELECT text FROM greetings WHERE id = '1' ")
    bot.send_message(message.chat.id, results)
    results = cursorConnectionAndRead("SELECT questionTEXT FROM First_4_questions")

    logging.info('The user %s started the registration process' % message.from_user.id)

    questioning(message)






def questioning(message):
    global results
    global myArray

    print(results)
    if results !=[]:
        for i in results:
            if len(results) == 1:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
                button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
                keyboard.add(button_phone)
                bot.send_message(message.chat.id,
                                 cursorConnectionAndRead("SELECT questionTEXT FROM First_4_questions WHERE questionID = 4 "),
                                 reply_markup=keyboard)
                bot.register_next_step_handler(message, questoningStep2_Except)


                break

            else:
                bot.send_message(message.chat.id,i)
                bot.register_next_step_handler(message,questoningStep2)
                del results[0]
                break
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True) #one_time_keyboard=True - спрятать кнопку после нажатия
        keyboard.add(*[types.KeyboardButton(name) for name in["Отправить"]])
        bot.send_message(message.chat.id, "Если все данные верны нажмите 'Отправить', в противном случае введите данные заново нажав на /start", reply_markup=keyboard)

        myArray[_db_Number_of_User]=message.from_user.id
        myArray.append("Грязь и мусор")
        myArray.append("Ямы")
        myArray.append("Неисправное освещение")
        myArray = tuple(myArray)




        bot.register_next_step_handler(message,finalStepOfRegistration)



def questoningStep2(message):

    myArray.append(message.text)

    questioning(message)

def questoningStep2_Except(message):
    global results

    try:
        print(message.contact.phone_number)
        myArray.append(message.contact.phone_number)
        del results[0]
        questioning(message)

    except:
        bot.send_message(message.chat.id,"Пожалуйста нажмите на кнопку")
        questioning(message)


def finalStepOfRegistration(message):
    global myArray

    if message.text == "Отправить":
        bot.send_message(message.chat.id,
                         'Поздравляю вы прошли регистрацию, ваша заявка находится на рассмотрении администрации')
        bot.send_message(message.chat.id,
                         'Используйте команду /start для того чтобы узнать ваш статус')

        print(myArray)
        cursorConnectionAndWrite("First_4_answers", myArray)
    else:
        start(message)




def cursorConnectionAndRead(sql):
    conn = sqlite3.connect('TZ_base.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    info = cursor.fetchall()
    conn.close()
    return info



def cursorConnectionAndWrite(tableName,insertingTurpleWithValues):                                  #очень простой вариант, лучше используй с
    conn = sqlite3.connect('TZ_base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO %s VALUES %s"%(tableName,insertingTurpleWithValues))
    conn.commit()
    conn.close()


def cursorConnectionAndUpdate(tableName,columnText,textValue,columnForOrientation,columnForOrientationValue):
    conn = sqlite3.connect('TZ_base.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE %s SET %s = '%s'  WHERE %s = '%s'" %(tableName,columnText,textValue,columnForOrientation,columnForOrientationValue))
    conn.commit()
    conn.close()





def considiration(message):
    bot.send_message(message.chat.id, cursorConnectionAndRead(
        "SELECT text_after_registration FROM RegistrationComplete WHERE tag = 'review_of_user'"))




def userRights(message):
    bot.send_message(message.chat.id, cursorConnectionAndRead(
        "SELECT text_after_registration FROM RegistrationComplete WHERE tag = 'user'"))

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ["О проекте", "Отправить сообщение", "Мои обращения", "Обратная связь"]])
    bot.send_message(message.chat.id,
                     "Выберите одну из функций по средству нажатия на одноименную кнопку",reply_markup=keyboard)
    bot.register_next_step_handler(message,UserButtonChoose)

def UserButtonChoose(message):


    if message.text == "О проекте":
        AboutProject(message)
        logging.info('the user selected the function "О проекте"')

    if message.text == "Отправить сообщение":
        SendMessage(message)
        logging.info('the user selected the function "Отправить сообщение"')

    if message.text == "Мои обращения":
        MyMessages(message)
        logging.info('the user selected the function "Мои обращения"')

    if message.text == "Обратная связь":
        ReverseConnection(message)
        logging.info('the user selected the function "Обратная связь"')

    if message.text =="/admin":
        adminModeActivation(message)


def AboutProject(message):     #функция создающая ссылку на сайт с информацией (доделать сайт)
    markup = types.InlineKeyboardMarkup()                               #кнопка будет редактироваться из режима админа
    btn_my_site = types.InlineKeyboardButton(text='Читать далее', url='http://telegra.ph/Stranica-vydelennaya-pod-oformlenie-informacii-dlya-DigitalCitizen-05-27')
    markup.add(btn_my_site)

    bot.send_message(message.chat.id, cursorConnectionAndRead("SELECT text FROM greetings WHERE id = '3'"), reply_markup=markup)
    userRights(message)

def SendMessage(message):
    global ConsistArray
    ConsistArray = []
    bot.send_message(message.chat.id,cursorConnectionAndRead("SELECT text FROM greetings WHERE id = 2"))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   [str(cursorConnectionAndRead("SELECT FavoriteCategory1 FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)[0][0]),
                    str(cursorConnectionAndRead("SELECT FavoriteCategory2 FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)[0][0]),
                    str(cursorConnectionAndRead("SELECT FavoriteCategory3 FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)[0][0]), "Показать все категории","Поменять избранные категории"]])

    bot.send_message(message.chat.id,"Выберите одну из функций по средству нажатия на одноименную кнопку",reply_markup=keyboard)
    bot.register_next_step_handler(message,SendMessageChoose1)



def SendMessageChoose1(message):
    global ConsistResult
    global OnefromFavorites

    connection = sqlite3.connect('TZ_base.db')
    cursor = connection.execute('select * from AllComplaints')
    ConsistResult = list(map(lambda x: x[0], cursor.description)) #как получить названия всех столбцов в таблице
    connection.close()

    if message.text == "Показать все категории":
        j = 1
        for i in cursorConnectionAndRead("SELECT Complaint_name FROM QuestionsForComplaints"):
            bot.send_message(message.chat.id,str(i[0]))
            j=j+1

        SendMessageChoose2(message)




    elif message.text == "Поменять избранные категории":
        global Favorites
        global OnefromFavorites

        Favorites = []
        j = 1
        for i in cursorConnectionAndRead("SELECT Complaint_name FROM QuestionsForComplaints"):
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Выбрать", callback_data=str(i[0]))
            keyboard.add(callback_button)
            bot.send_message(message.chat.id, str(i[0]) , reply_markup=keyboard)



            j = j + 1

    elif message.text == cursorConnectionAndRead("SELECT FavoriteCategory1 FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)[0][0]\
            or message.text == cursorConnectionAndRead("SELECT FavoriteCategory2 FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)[0][0]\
            or message.text == cursorConnectionAndRead("SELECT FavoriteCategory3 FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)[0][0]:


        OnefromFavorites = message.text
        SendMessageChoose2(message)




@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    global Favorites
    global UserID
    for i in cursorConnectionAndRead("SELECT Complaint_name FROM QuestionsForComplaints"):
        if c.data ==str(i[0]):
            print(str(i[0]))
            bot.send_message(c.message.chat.id,str(i[0]))
            Favorites.append(c.message.text)

    if len(Favorites) == 3:
        cursorConnectionAndUpdate("First_4_answers", "FavoriteCategory1", Favorites[0], "UserTelegrammID",UserID)

        cursorConnectionAndUpdate("First_4_answers", "FavoriteCategory2", Favorites[1], "UserTelegrammID",UserID)
        cursorConnectionAndUpdate("First_4_answers", "FavoriteCategory3", Favorites[2], "UserTelegrammID",UserID)
        userRights(c.message)










def SendMessageChoose2(message):
    global ConsistResult
    global ConsistArray
    global OnefromFavorites


    if ConsistResult != []:
        for i in ConsistResult:

            if i =="ConsistID":
                ConsistID_Except(message)


            elif i == "UserTelegrammID":
                UserTelegramm_Except(message)

            elif i == "Complaint" and OnefromFavorites != "":

                ConsistArray.append(OnefromFavorites)
                del ConsistResult[0]
                SendMessageChoose2(message)


            elif i == "PhotoOrVideo":
                PhotoOrVideo_Except(message)

            elif i == "Thanks":
                Thanks_Except(message)

            elif i == "Status":
                Status_Except(message)



            else:
                if i == "Complaint":
                    bot.register_next_step_handler(message,SendMessageErrorExcept)

                else:
                    bot.send_message(message.chat.id, "Write Your" + " " + i + ":")
                    OnefromFavorites = ""

                    bot.register_next_step_handler(message,SendMessageChoose3)



            break
    else:

        data = readImage(
        "%s" % ConsistArray[4])

        binary = sqlite3.Binary(data)




        conn = sqlite3.connect('TZ_base.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO AllComplaints (UserTelegrammID,Complaint,ComplaintPlace,ComplaintAddres,PhotoOrVideo,Comment,Thanks,Status) VALUES (?,?,?,?,?,?,?,?)", (ConsistArray[0],ConsistArray[1],ConsistArray[2],ConsistArray[3],binary,ConsistArray[5],ConsistArray[6],ConsistArray[7]))
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id,"Ваша заявка успешно отправлена рассмотрение")                                                             #("INSERT INTO Images(Data) VALUES (?)", (binary,) )




        userRights(message)


                                                                                    #ConsistID,UserTelegrammID,Complaint,ComplaintPlace,ComplaintAddres,PhotoOrVideo,Comment,Thanks,Status


def readImage(filename):
    fin = open(filename, "rb")
    img = fin.read()
    fin.close()
    os.remove(filename)
    return img




def SendMessageChoose3(message):

    ConsistArray.append(message.text)
    del ConsistResult[0]
    SendMessageChoose2(message)



def SendMessageErrorExcept(message):
    for i in cursorConnectionAndRead("SELECT Complaint_name FROM QuestionsForComplaints"):
        if str(i[0]) == message.text:
            ConsistArray.append(message.text)
            del ConsistResult[0]
            SendMessageChoose2(message)
            break

    else:
        bot.send_message(message.chat.id, "Такой категории не существует поробуйте еще раз")
        SendMessageChoose2(message)


def ConsistID_Except(message):
    del ConsistResult[0]
    SendMessageChoose2(message)

def UserTelegramm_Except(message):
    ConsistArray.append(message.from_user.id)
    del ConsistResult[0]
    SendMessageChoose2(message)

def PhotoOrVideo_Except(message):
    bot.send_message(message.chat.id,"Загрузите фото или видео")
    bot.register_next_step_handler(message,PhotoOrVideo_Except_Loading)




def PhotoOrVideo_Except_Loading(message):

    try:
        ConsistArray.append(message.photo[0].file_id)
        del ConsistResult[0]
        SendMessageChoose2(message)

        file_info = bot.get_file(message.photo[0].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = "/Users/Пользователь/Documents/GitHub/python/Дз по python/Дз8/ТЗ/" + message.photo[                       #путь сохранения добавь в конце /
            0].file_id
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

    except:
        bot.send_message(message.chat.id,"Неккоректный файл, попробуйте ещё раз")
        PhotoOrVideo_Except(message)















def Thanks_Except(message):
    ConsistArray.append("Отзыв отсутствует")
    del ConsistResult[0]
    SendMessageChoose2(message)


def Status_Except(message):
    ConsistArray.append("Заявка на рассмотрении")
    del ConsistResult[0]
    SendMessageChoose2(message)


def MyMessages(message):
    bot.send_message(message.chat.id,cursorConnectionAndRead("SELECT text FROM greetings WHERE id = 4"))
    for i in cursorConnectionAndRead("SELECT Complaint,Status FROM AllComplaints WHERE UserTelegrammID = %s" %message.from_user.id):
        bot.send_message(message.chat.id,"Жалоба: "+'"'+i[0]+'"' +"  Статус: "+'"'+i[1] +'"')
    message.from_user.id
    userRights(message)


def ReverseConnection(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Ссылка на наш сайт', url='http://telegra.ph/Stranica-vydelennaya-pod-oformlenie-informacii-dlya-DigitalCitizen-05-27')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, cursorConnectionAndRead("SELECT text FROM greetings WHERE id = 5"), reply_markup=markup)
    userRights(message)






def adminPasswordCheck(message):

    #из таблицы плучаем информацию в виде кортежа в списке, поэтому надо преобразовать в str через  [0][0]
    if  str(cursorConnectionAndRead("SELECT password FROM adminPassword")[0][0]) == message.text :
        cursorConnectionAndUpdate("First_4_answers","Status",AdminMode,"UserTelegrammID",message.from_user.id)
        bot.send_message(message.chat.id,"Теперь вы зарегистрированы как Админ и можете пользоваться привилегиями этого статуса")
        adminRights(message)
    else:
        bot.send_message(message.chat.id,"Введенный пароль не подходит")


def adminRights(message):
    logging.info('the user has been granted administrative rights')
    bot.send_message(message.chat.id,  cursorConnectionAndRead(
        "SELECT text_after_registration FROM RegistrationComplete WHERE tag = 'admin'"))

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)  # one_time_keyboard=True - спрятать кнопку после нажатия
    keyboard.add(*[types.KeyboardButton(name) for name in ["Ключевые слова", "Изменить 'Вопросы'","Редактировать текст","События","Участники группы","Вакансии"]])
    bot.send_message(message.chat.id,
                     "Для выбора функции нажмите на кнопку",
                     reply_markup=keyboard)

    bot.register_next_step_handler(message,AdminButtonChoose)


def AdminButtonChoose(message):


    if message.text == "Ключевые слова":
        textAfterRegistration(message)
        logging.info('the administrator selected the function  "Ключевые слова"')

    if message.text == "Изменить 'Вопросы'":
        KeyWords(message)                            #Меняет текст вопросов
        logging.info('the administrator selected the function  "Изменить Вопросы"')

    if message.text == "Редактировать текст":
        ChangeText(message)
        logging.info('the administrator selected the function  "Редактировать текст"')

    if message.text == "События":
        Developments(message)
        logging.info('the administrator selected the function   "События"')

    if message.text == "Участники группы":
        GroupMembers(message)
        logging.info('the administrator selected the function  "Участники группы"')

    if message.text == "Вакансии":
        Vacancies(message)
        logging.info('the administrator selected the function  "Вакансии"')


def KeyWords(message):      #функция для первой кнопки админа
    global results
    global myArray

    bot.send_message(message.chat.id,'Вы выбрали функцию"Ключевые слова" тперь вы можете изменить вопросы при регистрации пользователя.'
                                     'Вам по очереди будет выведен текст каждого вопроса, если вы захотите изменить его то просто отпрвьте текст с новым вопросом')

    results = cursorConnectionAndRead("SELECT questionID FROM First_4_questions")

    KeyWordsStep2(message)


def KeyWordsStep2(message):
    global i   #попытаться убрать этот костыль и разобраться с bot.register_next_ste_handler(может ли быть три аргумента)
    global results


    for i in results:

        bot.send_message(message.chat.id,"Редактируемый вопрос" + "<"+str(cursorConnectionAndRead("SELECT questionTEXT FROM First_4_questions WHERE questionID=%s" %i)[0][0])+">")
        bot.register_next_step_handler(message,KeyWordsStep3)
        del results[0]
        break







def KeyWordsStep3(message):
    global i
    try:
        i = i[0]
    except:
        print("'i' is already int")

    cursorConnectionAndUpdate("First_4_questions", "questionTEXT", message.text, "questionID", i)
    if results == []:
        bot.send_message(message.chat.id,"Вы поменяли текст вопросов при регистрациии")
        adminRights(message)
    KeyWordsStep2(message)



def textAfterRegistration(message):             #Функция для второй кнопки админа
    bot.send_message(message.chat.id,"Вы выбрали функцию изменить 'Ключевые слова', далее вам будт предоставлен исходный текст, чтобы изменить текст просто отправьте боту новый текст")
    bot.send_message(message.chat.id,cursorConnectionAndRead("SELECT text_after_registration FROM RegistrationComplete WHERE tag = 'user'"))
    bot.register_next_step_handler(message,textAfterRegistrationStep2)


def textAfterRegistrationStep2(message):
    cursorConnectionAndUpdate("RegistrationComplete", "text_after_registration", message.text, "tag", "user")
    adminRights(message)


def ChangeText(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)  # one_time_keyboard=True - спрятать кнопку после нажатия
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ["О проекте", "Отправить обращение", "Мои обращения", "Обратная связь","Назад"]])
    bot.send_message(message.chat.id,
                     "Для выбора функции нажмите на кнопку",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message,ChangeTextStep2)

def ChangeTextStep2(message):
    if message.text == "О проекте":
        bot.send_message(message.chat.id,"Введите сообщение которое будет выдаваться при нажатии кнопки 'O проекте'")
        bot.register_next_step_handler(message,ChangeTextStep3_1)

    if message.text == "Отправить обращение":
        bot.send_message(message.chat.id, "Введите сообщение которое будет выдаваться при нажатии кнопки 'Отправить обращение'")
        ChangeTextStep3_2(message)
    if message.text == "Мои обращения":
        bot.send_message(message.chat.id, "Введите сообщение которое будет выдаваться при нажатии кнопки 'Мои обращения'")
        ChangeTextStep3_3(message)
    if message.text == "Обратная связь":
        print(1)
    if message.text == "Назад":
        adminRights(message)

def ChangeTextStep3_1(message):
    cursorConnectionAndUpdate("greetings","text",message.text,"id",3)
    adminRights(message)

def ChangeTextStep3_2(message):
    cursorConnectionAndUpdate("greetings","text",message.text,"id",2)
    adminRights(message)

def ChangeTextStep3_3(message):
    cursorConnectionAndUpdate("greetings","text",message.text,"id",4)
    adminRights(message)

def ChangeTextStep3_4(message):
    cursorConnectionAndUpdate("greetings","text",message.text,"id",5)
    adminRights(message)




def Developments(message):
    bot.send_message(message.chat.id,"Функция не входит в ТЗ")
    adminRights(message)

def GroupMembers(message):
    bot.send_message(message.chat.id, "Функция не входит в ТЗ")
    adminRights(message)

def Vacancies(message):
    bot.send_message(message.chat.id, "Функция не входит в ТЗ")
    adminRights(message)








if __name__=='__main__':
    bot.polling(none_stop = True)




