import telebot
import config
import requests
import config
import vk

bot = telebot.TeleBot(config.token)
MY_USER_ID = ' '
session = vk.Session()
vkapi = vk.API(session)

predel = 0
friends_count = 0

@bot.message_handler(commands = ['start'])
def startFunction(message):
    bot.send_message(message.chat.id,"It's working: \nEnter your vk  id")
    

@bot.message_handler(content_types = ['text'])
def textFunction(message):
    global friends_count
    global predel
    MY_USER_ID = message.text
    p=vkapi.friends.get(user_id = MY_USER_ID,fields='uid,20first_name,%20last_name,%20sex,%20bdate,%20city,%20country,%20photo_200,%20online,%20lists,%20screen_name,%20contacts,%20education,%20universities,%20schools,%20activity,%20last_seen,%20relation,%20counters,%20nickname,%20relatives,%20interests,%20movies,%20tv,%20books,%20games,%20about,%20connections',v=5.74)

    
    if predel < 100:
        for x in p['items']:
            predel += 1
            print('Ищем друзей пользователя '+str(x['id']))
            bot.send_message(message.chat.id,"Ваши общие друзья с пользователем "+ str(x['first_name']+ ' ' +str(x['last_name']+':')))
            try:
                h = vkapi.friends.get(user_id = x['id'], fields='uid,20first_name,%20last_name,%20sex,%20bdate,%20city,%20country,%20photo_200,%20online,%20lists,%20screen_name,%20contacts,%20education,%20universities,%20schools,%20activity,%20last_seen,%20relation,%20counters,%20nickname,%20relatives,%20interests,%20movies,%20tv,%20books,%20games,%20about,%20connections',v=5.74)
                for z in p['items']:
                    for y in h['items']:
                        print(y['id'])
                        if z['id'] == y['id']:
                            friends_count +=1
                            bot.send_message(message.chat.id,str(y['first_name']+' '+str(y['last_name'])))
                        
            except:
                print('Error user')
            bot.send_message(message.chat.id,"Всего общих друзей: "+str(friends_count))      
        else:
            bot.send_message(message.chat.id,"Предел в сто друзей достигнут")
        friends_count = 0      





if __name__=='__main__':
    bot.polling(none_stop = True)
    
#Было очень интересно самому придумать алгоритм, пришлось ОЧЕНЬ хорошо подумать
