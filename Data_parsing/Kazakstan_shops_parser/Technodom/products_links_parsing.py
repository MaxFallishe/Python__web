from selenium import webdriver
import time

def main():
    
    browser = browser_activate()
    
    for url in ["https://www.technodom.kz/astana/catalog/notebooks","https://www.technodom.kz/astana/catalog/smartphones","https://www.technodom.kz/astana/catalog/kholodilniki","https://www.technodom.kz/astana/catalog/mikrovolnovye_pechi"]:
    #technodom_tv = 'https://www.technodom.kz/astana/catalog/led_televizory'
    
        browser.get(url)

        get_product_links(browser,"***")
        print('OK')




def browser_activate():
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()

    return browser

def get_product_links(browser,product_name):
    all_products = browser.find_elements_by_class_name("tda-product-grid__item")

    with open('product_links.txt','a') as file:
        file.write(product_name + '\n')
        for i in all_products:

            try:
                file.write(i.find_element_by_class_name("basetile__title").get_attribute("href")+'\n')

            except:
                pass

        

        
    









if __name__ == '__main__':
    main()
