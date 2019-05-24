from selenium import webdriver
import time
from time import strftime
import pymysql.cursors


def main():

    browser = browser_activate()
    
    connection = conn()

    shop = "Мечта"
    date = strftime("%Y-%m-%d")
    
    
    with open("product_links.txt") as file:
        for line in file.readlines():
            try:
            
                if line[0] != '*':
                    browser.get(line)
                            
                    product_model = browser.find_element_by_class_name("aa_header").find_element_by_tag_name("h1").text
                    try:
                        product_price = browser.find_element_by_class_name("ok_pr").text
                    except:
                        product_price = 'Нет в магазине'

                    product_price = product_price.replace(' ','')
                    
                    print("Product name: ", product_model)
                    #print("Price now: ", product_price)
                
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO products VALUES(Null,%s,%s,%s,%s,%s)",(shop, product_type,product_model,product_price,date))  
                        connection.commit()

                        cursor.close()
                        

                else:
                    product_type = line[1:].replace('\n', '')

            except:
                pass

    connection.close()  
            




def browser_activate():
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()

    return browser

def conn():
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             port = 3306,
                             password ='',
                             db = 'tutorial',
                             cursorclass = pymysql.cursors.DictCursor)
    return connection

    
 
    

    
if __name__ == '__main__':
    main()
