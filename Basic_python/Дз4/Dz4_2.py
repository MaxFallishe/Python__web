days =list(range(1,31+1))
holidays = [3,4]
for i in days:
    if i == holidays[0]:
        print('Выходной:'+str(i))
        holidays[0]+=7
    elif i == holidays[1]:
        print('Выходной:'+str(i))
        holidays[1]+=7
    else:   
        print('Рабочий:'+str(i))
