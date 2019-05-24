money = int(input("Начальная Сумма: "))
years = int(input("Срок депозита: "))
while years>0:
    money = money + (money*0.1)
    years -=1
print(money)
