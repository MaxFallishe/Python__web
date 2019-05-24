def bal():
    cost = input("""Как хотите провести бал:"Дёшего","Средне","Дорого" """)
    guests = int( input("Количество людей: "))
    if cost == "Дёшего":
        sumB=3000*guests
    elif cost == "Средне":
        sumB=3000*1.4*guests
    elif cost == "Дорого":
        sumB=3000*2*guests
    print(sumB)
bal() 
