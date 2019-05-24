import telebot
import config

bot = telebot.TeleBot(config.token)
egg = ""

@bot.message_handler(commands = ['start'])
def option_start(message):
    bot.send_message(message.chat.id,'Выберите категорию с помощью команды: \n /ground - первая группа \n /water - вторая группа \n /sky - третья группа  ')
    

@bot.message_handler(commands = ['ground'])
def option_ground(message):
    variable_change1()
    bot.send_message(message.chat.id,'Введите текст:')
    

@bot.message_handler(commands = ['water'])
def option_water(message):
    variable_change2()
    bot.send_message(message.chat.id,'Введите текст:')
    

@bot.message_handler(commands = ['sky'])
def option_sky(message):
    variable_change3()
    bot.send_message(message.chat.id,'Введите текст:')
   
    
@bot.message_handler(content_types = ['text'])
def textOption(message):
    bot.send_message(message.chat.id,message.text+' '+ egg)
   
def variable_change1():
    global egg
    egg = 'dry'
   
def variable_change2():
    global egg
    egg = 'wet'
 
def variable_change3():
    global egg
    egg = 'nothing'

if __name__=='__main__':
    bot.polling(none_stop = True)
