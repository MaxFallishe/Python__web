yourSum=0
sum200 = 0
sum500 = 0
sum1000 = 0
sum2000 = 0 
sum5000 = 0
sum10000 = 0
sum20000 = 0
while True:
    note = int(input("Введите купюру"))   
    if note == 200:
        sum200=sum200 + 1
        yourSum=yourSum+note
    elif note == 500:
        sum500=sum500 + 1
        yourSum=yourSum+note
    elif note == 1000:
        sum1000=sum1000 + 1
        yourSum=yourSum+note
    elif note == 2000:
        sum2000=sum2000 + 1
        yourSum=yourSum+note
    elif note == 5000:
        sum5000=sum5000 + 1
        yourSum=yourSum+note
    elif note == 10000:
        sum10000=sum10000 + 1
        yourSum=yourSum+note
    elif note == 20000:
        sum20000=sum20000 + 1
        yourSum=yourSum+note
        
    else:
        print("Неккоректная купюра")
        continue
    print("YourSum",yourSum)
    print("Купюр по 200",sum200)
    print("Купюр по 500",sum500)
    print("Купюр по 1000",sum1000)
    print("Купюр по 2000",sum2000)
    print("Купюр по 5000",sum5000)
    print("Купюр по 10000",sum10000)
    print("Купюр по 20000",sum20000)










    
        
