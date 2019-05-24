def kortezh():
    kolOfPupils = int(input("Введите кол-во человеков"))
    olivie = ('Картофель','Лук','Колбаса','Майонез','Огурцы','Морковь')
    gramm = (50*kolOfPupils,20*kolOfPupils,100*kolOfPupils,15*kolOfPupils,2*kolOfPupils,30*kolOfPupils)
    olivieF = (olivie[0]+': '+str(gramm[0]) +' gr',olivie[1]+': '+str(gramm[1]) +' gr',olivie[2]+': '+str(gramm[2]) +' gr',olivie[3]+': '+str(gramm[3]) +' gr',olivie[4]+': '+str(gramm[4]) +' gr')
    print(olivieF)
kortezh()    
    
#где можно использовать кортежи и в чем их преимущество?
