quantityOfNumber = int(input("Количество слагаемых: "))
yourSum = 0
while quantityOfNumber > 0:
    userCount = int (input("Число: "))
    yourSum = yourSum + userCount
    

    quantityOfNumber -= 1
print("Сумма = ",yourSum)    
