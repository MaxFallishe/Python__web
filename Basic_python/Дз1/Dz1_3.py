time = int(input("На сколько лет вы хотите офрмить кредит: "))
creditSum = int (input("Введите сумму кредита: "))
interestRate = int(input("Ваша процентная ставка: "))
firstContribution = int(input("Ваш первый взнос: "))

creditWithPercents = creditSum +(creditSum * interestRate/100)
monthlySum = creditWithPercents / time / 12
print("Ваш ежемесячый взнос: ",monthlySum)
