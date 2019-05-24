def time():
    yourTime = 0
    speed = 60
    distance = int(input("Введите расстояние"))
    yourTime = distance/speed * 60
    
    print(ci(yourTime))
    
def ci(num1):
    hour = num1 // 60
    minutes = num1 % 60
    hour = str(hour)
    minutes = str(minutes)
    if hour == "0.0":
        end=minutes+" Минут:"
        return end
    else:
        
        end= "Часов:"+hour+" Минут:"+minutes
        return end
   
    
    
time()

#Очень классное дз
    
    
