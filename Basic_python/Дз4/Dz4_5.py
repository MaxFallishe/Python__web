
def find():
    global film_list
    yourMovie = input("Введите название фильма:")
    for i in film_list:
        if yourMovie == i[0]:
            print(i)  
    else:
        print("Error")
        underMain()
        
def category():
    global film_list
    yourMovie = input("Введите категорию фильм:")
    for i in film_list:
        if yourMovie == i[2]:
            print("Фильм данной категории:"+str(i))
    else:
        print("Error")
        underMain()

def add():
    global film_list
    print("Для отмены добавления нового фильма введите exit")
    
    yourMovie_name = input("Введите название фильма")
    for i in film_list:
        if yourMovie_name == i[0]:
            print("Такое название фильма уже есть")
            underMain()
    exit(yourMovie_name)
    yourMovie_year = input("Введите год выхода фильма")
    exit(yourMovie_year)
    yourMovie_category = input("Введите жанр фильма")
    exit(yourMovie_category)
    yourMovie_rate = input("Введите рейтинг фильма")
    exit(yourMovie_rate)
    film_list.append([yourMovie_name,yourMovie_year,yourMovie_category,yourMovie_rate])
    
def delete():
    global film_list

    yourMovie = input("Введите название фильма который хотите удалить:")
    test = input("Yes - подтвердить, No - отмена: ")
    if test == "Yes":
        for i in film_list:
            if yourMovie == i[0]:
                film_list.remove(i)
    elif test == "No":
        underMain()    
    else:
        print("Error")
        underMain()
   
def print_list():
    for i in film_list:
        print(i)
        
def exit(a):
    if a == "exit":
        underMain()
  
def main():
    global film_list
    film_list = [["Побег из Шоушенка","1999","драма","9"],["Шрек","2001","мультфильм","8"],["Бэтмэн","2012","драма","8"]]
    underMain()
    
def underMain():
    while True:
        vvod = input("Введите атрибут \nfind - для поска фильма по названию \ncategory - для поиска фильмов по жанру \nadd - добавить фильм, \ndelete - удалить фильм\n")
    
        if vvod == "find":
            find()        
        elif vvod == "category":
            category()
        elif vvod == "add":
            add()
        elif vvod == "delete":
            delete()
        elif vvod == "print":
            print_list()
        else:
            print("Error")

while True:
    main()
    #очень сложные дз, но они того стоят
    
    
