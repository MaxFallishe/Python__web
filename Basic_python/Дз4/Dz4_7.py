countries = {"Казахстан":"17","Россия":"25","США":"23" }
def main():
    while True:
        name = input("Введите Страну")
        
        try:
            name = int(name)  
            print("Ошибка")
            main()
        except:       
            try:
                quantity = int(input("Введите численность"))
            except:
                print("Ошибка")
                main()
            
        countries[name] = quantity
        print(countries)

main()
