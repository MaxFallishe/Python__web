while True:
    year = input("Введите количество лет ")
    if year !=""  and year !="0":
        cat = year * 7
        dog = year * 3.64
        elephant = year * 1.14
        horse = year * 2

        print('По кошачьим меркам вам:',cat)
        print('По собачьим меркам вам:',int(dog))
        print('По слоновьему вам:',int(elephant))
        print('По лошадиным меркам вам:',horse)
    else:
        print("Error")
#Данные по соотношению возраста человека и животных взял с сайта https://wpcalc.com/konverter-vozrasta/
    
           
print("yay nice")