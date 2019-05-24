from selenium import webdriver
import time

def main():

    browser = browser_activate()

    for url in ['https://shop.kz/televizory/?PAGEN_1=1','https://shop.kz/noutbuki/?PAGEN_1=1','https://shop.kz/smartfony/?PAGEN_1=1','https://shop.kz/mikrovolnovki/?PAGEN_1=1','https://shop.kz/kholodilniki/filter/fltr_type-is-s_nizhney_morozilnoy_kameroy-or-c_verkhney_morozilnoy_kameroy/apply/?PAGEN_1=1']:

        with open('product_links.txt','a') as file:
                file.write("*" + '\n')

                
        for i in range (1,2+1):
            
            

            

            browser.get(url[:-1]+str(i))

            get_product_links(browser)
                








def browser_activate():
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()

    return browser


def get_product_links(browser):
    all_products = browser.find_elements_by_class_name("bx_catalog_item")

    with open('product_links.txt','a') as file: 
        for i in all_products:
            
            #file.write(i.find_element_by_class_name("bx_catalog_item_title").find_element_by_tag_name("'a'").get_attribute("href")+'\n')
            file.write(i.find_element_by_class_name("bx_catalog_item_images").get_attribute("href")+'\n')
            print(i.find_element_by_class_name("bx_catalog_item_images").get_attribute("href"))





if __name__ == '__main__':
    main()
