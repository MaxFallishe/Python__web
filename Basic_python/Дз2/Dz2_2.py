docs = int(input("Введите кол-во страниц документа"))
if docs<=0:
   print("Error")
else:   
   page = 1
   while page <= docs:
      print("Страница номер: ",page)       
      print("Подача бумаги")
      print("Нанесение краски")
      print("Вывод бумаги")
      page  += 1
   print("Печать завершена")
