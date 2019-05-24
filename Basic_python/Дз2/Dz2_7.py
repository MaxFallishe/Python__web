def calc():
    averageIncom = 0
    monthes = int(input("Количество месяцев"))
    tm = monthes
    while monthes > 0:
        month = int(input("Введите число: "))
        averageIncom = month + averageIncom
        monthes -=1

    averageIncom =averageIncom/tm
    print("Cредний доход: ",averageIncom)
calc()
    
