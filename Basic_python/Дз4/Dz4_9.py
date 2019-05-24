countries = {"Казахстан":{"Численность":"17","Столица":"Астана","Площадь":"2725000","Города":{"Астана": "815000","Алматы": "1800000"}},"Россия":{"Численность":"144","Столица":"Москва","Площадь":"17100000","Города":{"Москва": "7560000","Санкт-Петербург":"6300000"}},"США":{"Численность":"325","Столица":"Вашингтон","Площадь":"29834000","Города":{"Лос-Анджелес:" "9810000","Техас: 2700000"}}}


def main():
    while True:
        switch = input("Введите комманду:\nadd - добавить страну \ndelete - удалить страну\nprint - вывести все элементы списки\n")
        if switch == "add":
            add()                                                                                           
        if switch == "delete":
            delete()
        if switch == "print":
            print_dict()
        else:
            print("Error")
            main()
            
def add():
    country_name = input("Введите название страны")
    country_pupils = input("Введите численность")
    country_capital = input("Введите столицу")
    country_S = input("Введите площадь")
    country_cities_count = int(input("Сколько городов хотите добавить?"))
    
    
   

    while country_cities_count > 0:
        city_name = input("Название города")
        city_humans = input("Количество населения")
        countries.update ({country_name:{"Численность":country_pupils,"Cтолица":country_capital,"Площадь":country_S,"Города":{city_name:city_humans}}})

        country_cities_count -= 1                                                                                  


def delete():
    element = input("Введите страну которую хотите удалить")
    
    


def print_dict():
   for key, value in countries.items():
    print(key, "-", value)


main() 
