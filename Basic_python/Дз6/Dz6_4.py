#если есть какие-то доп. условия пожалуйста допишите я доделаю(делаю как написано в руководстве)
import random

players_top = {'Нагибатор2009':str(random.randint(0,100))+' очков','Убивака':str(random.randint(0,100))+' очков','Дарккиллер':str(random.randint(0,100))+' очков'}
traveling = {'Казахстан':'4 балла','Россия':'5 баллов','Америка':' 5 баллов'}
while True:
    choise = input('Введите комманду: \nрейтинг - для вывода топ игроков \nпутешествие - для вывода стран и их оценок \n')

    if choise == 'рейтинг':
        for i in players_top:
            print(i + ' ' +players_top[i])
        print('\n')
    elif choise == 'путешествие':
         for i in traveling:
            print(i + ' ' +traveling[i])
         print('\n')
    else:
        print('Ошибка ввода')
        print('\n')
for i in players_top:
    print(i + ' ' +players_top[i])
