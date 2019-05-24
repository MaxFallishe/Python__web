#Hедавно для себя запилил похожий тест на C# буду рад если посмотрите - https://drive.google.com/file/d/1NAgaNhe8DmSAlucWQSSsCKT2ZqUMOU-H/view 

questions_mas = ['1. 5+5=','2. 2*2=','3. (5+3)/2=','4. 88+(13*2)=','5. 35/7+2*5=']
answer_1var_mas =['1)10','1)4','1)1','1)114','1)255']
answer_2var_mas = ['2)30','2)6','2)4','2)94','2)13']
answer_3var_mas = ['3)25','3)1','3)16','3)116','3)15']
right_answers = ['1','1','2','1','3']

count = 0
your_score = 0


def change():
    global count
    global your_score
    
    print(questions_mas[count])
    print(answer_1var_mas[count])
    print(answer_2var_mas[count])
    print(answer_3var_mas[count])

    if right_answers[count] == input("Введите ответ:"):
        print('Good')
        your_score +=1
    else:
        print('Bad')
    
    count+=1

    
for i in range(5):
    change()
    
print("Ваш счёт: ",your_score)


    

    
