list_of_students=[]
print('Чтобы вывести список студентов напишите inf')
while True:
    cmd = ''
    inf = 'inf'
    student = input('Введите имя нового студента')
    if student == inf:
        print(list_of_students)
        continue
    for i in list_of_students:
         
        if i == student:
            print('Такой студент уже есть \ndelete - удалить студента \nback - вернуться к списку')
            cmd = input('Введите команду: ')
            if cmd == 'delete':
                 list_of_students.remove(student)
            elif cmd == 'back':
                break
            else:
                print('Error')
            break
    else:
        if student == inf:
            print(list_of_students)
        print('add - добавить ученика \nback - вернуться к списку')
        cmd = input('Введите команду: ')
        if cmd == 'add':
            list_of_students.append(student) 

        elif cmd == 'back':
                break
        else:
            print('Error')
    print(list_of_students)
        
    
