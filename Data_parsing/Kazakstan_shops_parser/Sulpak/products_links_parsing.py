from selenium import webdriver

def main():

    browser = browser_activate()

    for url in ['https://www.sulpak.kz/f/led_oled_televizoriy', 'https://www.sulpak.kz/f/noutbuki', 'https://www.sulpak.kz/f/smartfoniy' ,'https://www.sulpak.kz/f/mikrovolnoviye_pechi']:
 
        browser.get(url)
        
        get_product_links(browser,"***", "tile-container", "title")


    for url in ['https://www.sulpak.kz/f/holodilniki']:
        browser.get(url)

        all_products = browser

        get_product_links(browser,"***", "goods-list-item", "title")


def browser_activate():
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()

    return browser



def get_product_links(browser, product_name, product_container_class_name, href_class_name):
    all_products = browser.find_elements_by_class_name(product_container_class_name)

    with open('product_links.txt','a') as file:
        file.write(product_name + '\n')
        for i in all_products:

            try:
                file.write(i.find_element_by_class_name(href_class_name).get_attribute("href")+'\n')

            except:
                pass










if __name__ == '__main__':
    main()
