def main():
    report = []
    AllProfit = 0
    maxInc=[]
    minInc=[]
    maxCon=[]
    minCon=[]
    maxNetProfit=[]
    minNetProfit=[]
    
    print("Вас приветствует программа для составления годового отчета, вам необходимо заполнить 12 месяцев")
    while len(report) < 3:
        month = input('Введите месяц')
        income = int(input('Введите доход за месяц'))
        consumption =int(input('Введите расход за месяц'))
        net_profit = income - consumption
        report.append([month,income,consumption,net_profit])
    

    for i in report:
        
        maxInc.append([i[1]])
        minInc.append([i[1]])
        maxCon.append([i[2]])
        minCon.append([i[2]])
        maxNetProfit.append([i[3]])
        minNetProfit.append([i[3]])
        AllProfit +=net_profit
        
   
    print("Чистая прибыль за весь год:"+str(AllProfit))
    print("Максимальная прибыль за месяц без расходов:"+str(max(maxInc)))
    print("Минимальная прибыль за месяц без расходов:"+str(min(minInc)))
    print("Максимальные расходы за месяц:"+str(max(maxCon)))
    print("Минимальные расходы за месяц:"+str(min(minCon)))
    print("Максимальная чистая прибыль за месяц:"+str(max(maxNetProfit)))
    print("Минимальная чистая прибыль за месяц"+str(min(minNetProfit)))
main()
#Допилить функции удаления и редактиования
