import math
a = int(input("Введите число a:" ))
b = int (input("Введите число b:"))
c = int (input("Введите число c:"))

D = b ** 2 - 4 * a * c
print(D)
if D < 0:
  print("Корней нет")
elif D == 0:
  x = -b / 2 * a
  print ("Корень = ",x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print("Первый корень: ",x1)
  print("Второй корень: ",x2)
#Пришлось использовать модуль 'math' и возведение в степень '**'
