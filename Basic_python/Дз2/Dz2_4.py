start = int(input("Первое значение: "))
finish = int(input("Последнее значение: "))
shag = int(input("Шаг: "))



for i in range(start, finish + 1, shag):
	print(i)
