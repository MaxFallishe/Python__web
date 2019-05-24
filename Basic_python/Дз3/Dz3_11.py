import telebot
import config

bot = telebot.TeleBot(config.token)

add_or_del = False
number_of_group = 1

group_1 = ['Вася','Петя','Митя']
group_2 = ['Кот','Собака','Корова']
group_3 = ['Картошка','Помидоры','Огурцы']

@bot.message_handler(commands = ['start'])
def startFunc(message):
    bot.send_message(message.chat.id,'Выберите группу \n 1./group1 \n 2./group2 \n 3./group3 \n')
@bot.message_handler(commands = ['group1'])

def group_1_Func(message):
    global number_of_group
    number_of_group = 1
    for i in group_1:
        bot.send_message(message.chat.id,i)
    bot.send_message(message.chat.id,'/add - добавить элемент, \n /del - удалить элемент')


@bot.message_handler(commands = ['group2'])
def group_2_Func(message):
    global number_of_group
    number_of_group = 2
    for i in group_2:
        bot.send_message(message.chat.id,i)
    bot.send_message(message.chat.id,'/add - добавить элемент, \n /del - удалить элемент')


@bot.message_handler(commands = ['group3'])
def group_3_Func(message):
    global number_of_group
    number_of_group = 3
    for i in group_3:
        bot.send_message(message.chat.id,i)
    bot.send_message(message.chat.id,'/add - добавить элемент \n /del - удалить элемент')


        
@bot.message_handler(commands = ['add']) 
def add_Func(message):
    global add_or_del
    
    add_or_del = True
    bot.send_message(message.chat.id,'Введите атрибут который хотите добавить')

        
@bot.message_handler(commands = ['del']) 
def del_Func(message):
        global add_or_del

        add_or_del = False
        bot.send_message(message.chat.id,'Введите атрибут который хотите удалить')
    
@bot.message_handler(content_types = ['text'])
def handler_of_text(message):
    if add_or_del == True:
        if number_of_group == 1:
            group_1.append(message.text)
            for i in group_1: 
                bot.send_message(message.chat.id,i)
                
        if number_of_group == 2:
            group_2.append(message.text)
            for i in group_2: 
                bot.send_message(message.chat.id,i)
               
        if number_of_group == 3:
            group_3.append(message.text)
            for i in group_3: 
                bot.send_message(message.chat.id,i)
                
    else:
        if number_of_group == 1:
            group_1.remove(message.text)
            for i in group_1: 
                bot.send_message(message.chat.id,i)
                
        if number_of_group == 2:
            group_2.remove(message.text)
            for i in group_2: 
                bot.send_message(message.chat.id,i)
               
        if number_of_group == 3:
            group_3.remove(message.text)
            for i in group_3: 
                bot.send_message(message.chat.id,i)
        
        







if __name__ == '__main__':
    bot.polling(none_stop = True)
