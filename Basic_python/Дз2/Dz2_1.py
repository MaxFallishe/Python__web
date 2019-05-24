start = int(input("Введите значение start"))
end = int(input("Введите значение end"))
if end < start:
    print("Error")
else:
    shag  = int(input("Введите шаг"))
    while start < end+1:
            print(start)
            start += shag


