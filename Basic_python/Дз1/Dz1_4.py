contributionSum = int(input("Введите сумму вклада: "))
interestRate = int(input("Введите процентную ставку: "))
depositDuration = int (input("Введите длительность Вклада: "))


profitAMonth = contributionSum *(interestRate/100)
allProfit = depositDuration * profitAMonth

print("Доход в месяц: ",profitAMonth)
print("Доход за все время депозита: ",allProfit)

#Непонятна фраза 'срок вклада в месяц', если я понял правильно то это то,
#насколько  месяцев вкладчик оставляет его в банке, но зачем этот пункт если
#можно посчитать без него, на всякий случай я посчитал весь доход за все время вклада

