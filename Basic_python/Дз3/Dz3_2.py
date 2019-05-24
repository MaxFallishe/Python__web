list_of_students=['Никита','Рома','Катя','Лена','Богдан','Диасдастан','Кирилл','Влад','Стас']
vvod = int(input('Введите число'))
if vvod <= 0 or vvod > 9:
    print('Error')
else:                    
    print(list_of_students[vvod-1])
