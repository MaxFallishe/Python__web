import telebot 
import config

bot = telebot.TeleBot(config.token)

a_d_p_f = ''

time = ''
list_of_students=['Никита','Рома','Катя','Лена','Богдан','Диасдастан','Кирилл','Влад','Стас']


   

@bot.message_handler(commands = ['start'])
def start_Func(message):
    bot.send_message(message.chat.id,'Выберите функцию: \n /add - Добавить студента \n /delete - Удалить студента \n /pin - Вывести весь список студентов \n /find - Найти ученика')

@bot.message_handler(commands = ['add'])
def handler_add(message):
    global a_d_p_f
    bot.send_message(message.chat.id,'Введите имя ученика')
    a_d_p_f = 'add'
    

@bot.message_handler(commands = ['delete'])
def handler_delete(message):
    bot.send_message(message.chat.id,'Введите имя ученика или его номер')
    global a_d_p_f
    a_d_p_f = 'del'

@bot.message_handler(commands = ['pin'])
def handler_pin(message):
    bot.send_message(message.chat.id,'Все ученики: ')
    pin(message)
    
    
@bot.message_handler(commands = ['find'])
def handler_find(message):
    
    global a_d_p_f

    bot.send_message(message.chat.id,'Введите имя ученика или его номер')
    a_d_p_f = 'find'

@bot.message_handler(content_types = ['text'])
def time_variable(message):
    global time
    if a_d_p_f == 'add':
        time = message.text
        add()
    if a_d_p_f == 'del':
        time = message.text
        deleting()
    if a_d_p_f == 'find':
        time = message.text
        find(message)
        
    
   

    

def add():
    global time
    
    list_of_students.append(time)
    
    
def deleting():
    global time
    try:
       
        time = int(time)        
        del list_of_students[time-1]
       
        
    except:
        list_of_students.remove(time)
        
def pin(message):    
    for i in list_of_students: 
        bot.send_message(message.chat.id,i) #Вывод студентов с помощью массива
    
def find(message):
    global time
    
    try:
        time = int(time)
        bot.send_message(message.chat.id,list_of_students[time-1])
        
    except:
        bot.send_message(message.chat.id,list_of_students[list_of_students.index(time)])
       
        
if __name__ == '__main__':
    bot.polling(none_stop = True)

