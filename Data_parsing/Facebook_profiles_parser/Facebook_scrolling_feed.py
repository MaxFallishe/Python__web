from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import sqlite3
import time
import random

def main():
     email_for_auth = "n13b@inbox.ru"
     password_for_auth = "Bvadimnik"


     comments = ["lol, Okay", "Yes, I'm agree", "Not Fun", "Impossible to imagine", "I don't know",
                 "SO strange", "so strange","I wonder...", "I think this isn't my favorite post",
                 "Good think","You explode my brain", "I can't...","No way","Not in this life",
                 "The Powerfull", "My friends will approve", "and you?", "but... I...", "Maybe",
                 "Just smile", ":-)", "OK", "Perfecto","WHAAAT?!","Don't stand a pillar", "yes yes yes",
                 "no no no", "what to do...", "ohhhh","Pretty good","Im believe","(:)_(:)"
                 "unbelievable"]
     
     browser = browser_ad()

     auth(browser,email_for_auth,password_for_auth)

     browser.get("https://www.facebook.com/groups/843804142348443/")
     
     scroll_page(browser,60,2)



def browser_ad():
    options = Options()
    options.add_argument("--disable-notifications")
    
    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe", chrome_options=options)
    browser.maximize_window()

    return browser


def auth(browser,email,password):
    url_for_auth = "https://www.facebook.com"
    browser.get(url_for_auth)
    
    email = browser.find_element_by_id('email')
    password = browser.find_element_by_id('pass')
    enter_button = browser.find_element_by_class_name('uiButton')

    email.send_keys("n13b@inbox.ru")
    password.send_keys("Bvadimnik")
    enter_button.click()


def comment(broowser, text):
    pass


def scroll_page(browser, scroll_time ,scroll_pause_time):
     #scroll_time and scroll_pause_time must be in units of measurement - 'seconds'
    
     time_start = time.time()

     start_value = 500
     while True:
          #Generate the random length of news feed scrolling 
          browser.execute_script("window.scrollTo(0, %s)" % random.randint(start_value, start_value + 1000)) 


          like_buttons = browser.find_elements_by_class_name('UFILikeLink')
          print("Like buttons count: ",len(like_buttons))

        
          like_buttons_count = len(like_buttons)

          random_like = random.randint(1,like_buttons_count-1) #Доработать алгоритм
          like_button = like_buttons[random_like] 

        
          chance = random.randint(1,100)
          print(chance,"%")
          if chance <= 10:
               try:
                    like_button.click()
                    print("Liked successfully")
               except:
                    print("Eror: isn't liked")
        
        
          start_value += 1000
        
          
        
          time.sleep(1)
    
     comm = '''
    while True:

        if time.time() >= time_start + scroll_time:

            break
         
        try:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
                        
            last_height = new_height
    
        except:
            pass
        
        time.sleep(scroll_pause_time)
    '''



if __name__ == '__main__':
    main()






