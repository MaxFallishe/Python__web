from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import sqlite3
import time


def main():
    options = Options()
    options.add_argument("--disable-notifications")

    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe", chrome_options=options)
    browser.maximize_window()

    url = "https://www.facebook.com"
    browser.get(url)

    email = browser.find_element_by_id('email')
    password = browser.find_element_by_id('pass')
    enter_button = browser.find_element_by_class_name('uiButton')

    email.send_keys("n13b@inbox.ru")
    password.send_keys("Bvadimnik")
    enter_button.click()



    with open("All_names.txt") as file:
        for line in file.readlines():
    
            test_url = "https://www.facebook.com/search/str/" + line + "/keywords_users"

            browser.get(test_url)
            
            i = 0
            SCROLL_PAUSE_TIME = 3

            # Get scroll height
            last_height = browser.execute_script("return document.body.scrollHeight")

            while True:
                if i == 100:
                    break
                
                try:
                    # Scroll down to bottom
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = browser.execute_script("return document.body.scrollHeight")
                    
                    
                    last_height = new_height


                    container = browser.find_element_by_id('fbBrowseScrollingPagerContainer'+str(i))
                    print('fbBrowseScrollingPagerContainer'+str(i))
                    time.sleep(2)
                    links = container.find_elements_by_class_name('_32mo')
                    
                    for j in links:
                        with open('Profiles.txt','a') as file2:
                            file2.write(j.get_attribute("href")+'\n')
                            
                        print(j.get_attribute("href"))
                        
                    
                except:
                    pass
                
                i+=1
                




















if __name__ == '__main__':
    main()
