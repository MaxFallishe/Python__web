from selenium import webdriver
import time

def main():

    browser = browser_activate()
    
    for url in ["https://www.mechta.kz/section/televizory/?sort=popular&adesc=desc&PAGEN_2=",
                "https://www.mechta.kz/section/noutbuki/?sort=popular&adesc=desc&PAGEN_2=",
                "https://www.mechta.kz/section/smartfony/?sort=popular&adesc=desc&PAGEN_2=",
                "https://www.mechta.kz/section/holodilniki/?sort=popular&adesc=desc&PAGEN_2=",
                "https://www.mechta.kz/section/mikrovolnovye-pechi/?sort=popular&adesc=desc&PAGEN_2="]:

        with open('product_links.txt','a') as file:
            file.write("*" + '\n')

        
        for i in range(1,3+1):

            

            browser.get(url+str(i))

            get_product_links(browser)






def browser_activate():
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()

    return browser


def get_product_links(browser):
    all_products = browser.find_elements_by_class_name("aa_sectiontov")

    with open('product_links.txt','a') as file:
        file.write(product_name + '\n')
        for i in all_products:
            
            try:
                file.write(i.find_element_by_class_name("ifont110").get_attribute("href")+'\n')
                print(i.find_element_by_class_name("ifont110").get_attribute("href"))
            except:
                pass


if __name__ == '__main__':
    main()
