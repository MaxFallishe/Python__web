def add():
    student = input('Введите имя или номер: ')
    list_of_students.append(student)
    print(list_of_students)
def deleting():
    student = input('Введите имя или номер: ')
    try:
        student = int(student)        
        del list_of_students[student]
        print (list_of_students)
        
    except:
        list_of_students.remove(student)
        print(list_of_students)
def enter():
    
    print(list_of_students)
def find():
    student = input('Введите имя или номер: ')
    try:
        student = int(student)
        print(list_of_students[student - 1])
    except:
        list_of_students.index(student)
        print(list_of_students[list_of_students.index(student)])

list_of_students=['Никита','Рома','Катя','Лена','Богдан','Диасдастан','Кирилл','Влад','Стас']
change = int(input(' 1. Добавить ученика,\n 2. Удалить ученика,\n 3.Вывести весь список ученика,\n 4.Найти ученика\n Выбeрите функцию:'))

if change == 1:
    add(student)
    
if change == 2:   
    deleting()
    
if change == 3:
    enter()
    
if change == 4:    
    find()

# Пришлось изучить функцию del детальнее

    
    
    
