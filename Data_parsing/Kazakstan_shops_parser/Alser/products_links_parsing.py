from selenium import webdriver
import time

def main():
    browser = browser_activate()


    for url in ["https://alser.kz/c/vse-televizory?sort=popular&per_page=32",
                "https://alser.kz/c/vse-noutbuki?sort=popular&per_page=32",
                "https://alser.kz/c/vse-smartfony?sort=popular&per_page=32",
                "https://alser.kz/c/mikrovolnovye-pechi?sort=popular&per_page=32",
                "https://alser.kz/c/holodilniki-dlja-bytovoi-tehniki?sort=popular&per_page=32"]:
        
        with open('product_links.txt','a') as file:
                file.write("*" + '\n')

        browser.get(url)

        get_product_links(browser)
        



def browser_activate():
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()

    return browser


def get_product_links(browser):
    all_products = browser.find_elements_by_class_name("good-item-title")

    with open('product_links.txt','a') as file: 
        for i in all_products:
            
            #file.write(i.find_element_by_class_name("bx_catalog_item_title").find_element_by_tag_name("'a'").get_attribute("href")+'\n')
            file.write(i.find_element_by_tag_name("a").get_attribute("href")+'\n')
            print(i.find_element_by_tag_name("a").get_attribute("href"))


if __name__ == '__main__':
    main()
