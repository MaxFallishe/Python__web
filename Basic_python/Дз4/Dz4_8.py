countries = {"Казахстан":{"Численность":"17","Столица":"Астана","Площадь":"2725000"},"Россия":{"Численность":"144","Столица":"Москва","Площадь":"17100000"},"США":{"Численность":"325","Столица":"Вашингтон","Площадь":"29834000"}}


def main():
    while True:
        switch = input("Введите комманду:\nadd - добавить страну \ndelete - удалить страну\n")
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
    countries[country_name] = {"Численность":country_pupils,"Столица":country_capital,"Площадь":country_S}
                                                                                      


def delete():
    element = input("Введите страну которую хотите удалить")
    
    


def print_dict():
    for key, value in countries.items():
        print(key, "-", value)


main() 
