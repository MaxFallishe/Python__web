import telebot
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def option_start(message):
    bot.send_message(message.chat.id,'Введите команду: \n /cities - для вывода Городов РК, \n /students - для вывода всех учеников, \n /sights - для вывода достопримечательностей Астаны')
    print('OK')

@bot.message_handler(commands=['cities'])
def option_cities(message):
    bot.send_message(message.chat.id,'Астана, Алматы, Актау, Атырау, Актобе, Актау, Караганды, Кокшетау, Кызылорда, Павлодар, Петропавловск, Семей, Талдыкорган, Темиртау, Экибастуз')
    
@bot.message_handler(commands=['students'])
def option_students(message):
    bot.send_message(message.chat.id,'Никита, Рома, Катя, Лена, Богдан, Диасдастан, Кирилл, Влад, Стас') 
    
@bot.message_handler(commands=['sights'])
def option_sights(message):
    bot.send_message(message.chat.id,'Байтерек, Музей первого президента Казахстана, Дворец мира и согласия, Ак Орда, Атамекен, Думан, Хан-Шатыр, Мечеть Хазрет-Султан, Цирк       ')





if __name__=='__main__':
    bot.polling(none_stop = True)














#Бот с именем Reinghart
