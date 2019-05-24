list_of_students=[]
while True:
    student = input('Введите имя нового студента')
    for i in list_of_students:
        if i == student:
            print('Такой студент уже есть')
            break
    else:
        list_of_students.append(student)
        print(list_of_students)
