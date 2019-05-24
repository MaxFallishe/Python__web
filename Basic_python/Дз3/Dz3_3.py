list_of_students=[['Никита',2,11.5],['Рома',3,11.0],['Катя',3,10.5],['Лена',4,10.0],['Богдан',5,9.5],['Диасдастан',6,9.0],['Кирилл',7,8.5],['Влад',8,8.0],['Стас',9,7.5]]
vvod = input('Введите аргумент:')
count = 0

try:
    vvod = int(vvod)
    for i in list_of_students:
        if list_of_students[count][1] == vvod:
            print(list_of_students[count])
        count +=1
   
   
except:
    count = 0 
    for i in list_of_students:
        if list_of_students[count][0] == vvod:
            print(list_of_students[count])
        count +=1

#Не помню так ли мы это делали в классе, но в любом случае я сам пришел к этому решению        
                
            
