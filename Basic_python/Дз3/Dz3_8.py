holNum = int (input('1.Новый год\n2.Наурыз\n3.8Марта\n4.7 Мая\n5.День Столицы\n'))
groupNum = int (input('1.Руководство \n2.Администрация \n3.Бухгалтерия \n4.Отдел продаж \n5.Программисты\n'))
finalHolidays = 0

holidays = ('Новый год ', 'Наурыз ','8 Марта ','7 Мая','День Столицы ')
group = ('Руководство','Администрация','Бухгалтерия','Отдел продаж','Программисты')
holidaysDays = [3,2,3,3,1]



def treatment(x,y):
    index = x-1
    if holidaysDays[index] >= 3:     
        if groupNum == 3:       
           finalHolidays = holidaysDays[index]
        elif groupNum == 2:        
            finalHolidays = holidaysDays[index]-1
        elif groupNum == 1:          
            finalHolidays =holidaysDays[index]-2
    if groupNum > 3:
       finalHolidays = holidaysDays[index]+1     
    print(finalHolidays)
        



















 
        


#1-ый вариант         
'''    if y == 1:        
        if holidaysDays[index] >=3:
           print(holidaysDays[index] - 2)
        else:
            print(holidaysDays[index])            
    if y == 2:     
        if holidaysDays[index] >=3:
           print(holidaysDays[index] - 1)
        else:
            print(holidaysDays[index])            
    if y == 3:
        print(holidaysDays[index])      
    if y == 4:
        print(holidaysDays[index]+1)        
    if y == 5:      
       print(holidaysDays[index]+1) '''
 
        
    
treatment(holNum,groupNum)    















