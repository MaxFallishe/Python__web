def calc():
    count =  int(input("Введите число"))
    power = input("Введите степен")
    if(power==""):
        eq = count ** 2
        print (eq)
    else:
        power = int(power)
        eq = count ** power
        print(eq)
calc()
