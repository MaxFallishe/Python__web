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
    
    browser = browser_ad()
    auth(browser,email_for_auth,password_for_auth)

    pause_time = 100
    cycles_count = 1
    
    with open("Profiles.txt") as file:    
        for line in file.readlines():
            try:
                print(cycles_count, "cycle is start")
                    
                get_user_inf(browser,line)
                    
                print(cycles_count, "cycle is successful")
                    
                cycles_count +=1
            except:
                print("Unaviable to save account information")

            watch_acc_feed(browser,pause_time)
            #time.sleep(pause_time)
            
            
        


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

    #n13b@inbox.ru
    #Bvadimnik

    
    
    
    email.send_keys("n13b@inbox.ru")
    password.send_keys("Bvadimnik")
    enter_button.click()


def get_user_inf(browser,user_url):
    about_link = "/about?"
    friends_link = "/friends?"
    checkins_link = "/map?"
    sports_link = "/sports?"
    music_link = "/music?"
    movies_link = "/movies?"
    tv_link = "/tv?"
    books_link = "/books?"
    likes_link = "/likes?"
    reviews_link = "/reviews?"

    
    browser.get(user_url)
    #print('check_1')

    scroll_page(browser,50,1)
    user_posts_inf = get_all_user_posts(browser)

    
    user_name = browser.find_element_by_class_name('_2nlw').text
    raw_link = browser.find_element_by_class_name('_6-6').get_attribute("href")
    build_link_elements = raw_link.split('?')

    build_link_elements[0] = build_link_elements[0].replace("/timeline","")
    
    #print(build_link_elements[0])
    #print(about_link)
    
    user_about_inf = get_user_about(browser, build_link_elements[0], about_link, build_link_elements[1])
    #print('check_2')

    #Not so right
    work_and_education = user_about_inf[0]
    lived_places = user_about_inf[1]
    contacts = user_about_inf[2]
    relation_ships = user_about_inf[3]
    details = user_about_inf[4]
    life_events = user_about_inf[5]
    
    #print(1)
    user_friends_inf = get_user_more(browser,build_link_elements[0],
                                     friends_link, build_link_elements[1])  
    
    #print(2)
    user_checkins_inf = get_user_more(browser,build_link_elements[0],
                                      checkins_link,build_link_elements[1])

    #print(3)
    user_sports_inf = get_user_more(browser,build_link_elements[0],
                                    sports_link,build_link_elements[1])

    #print(4)
    user_music_inf = get_user_more(browser,build_link_elements[0],
                                   music_link,build_link_elements[1])

    #print(5)
    user_movies_inf = get_user_more(browser,build_link_elements[0],
                                    movies_link,build_link_elements[1])

    #print(6)
    user_tv_inf = get_user_more(browser,build_link_elements[0],
                                tv_link,build_link_elements[1])

    #print(7)
    user_books_inf = get_user_more(browser,build_link_elements[0],
                                   books_link,build_link_elements[1])

    #print(8)
    user_likes_inf = get_user_more(browser,build_link_elements[0],
                                   likes_link,build_link_elements[1])

    #print(9)
    user_reviews_inf = get_user_more(browser,build_link_elements[0],
                                     reviews_link,build_link_elements[1])
    #print('check_3')
    user_data = [(user_name,work_and_education,lived_places,contacts,
                 relation_ships,details,life_events,user_friends_inf,
                 user_checkins_inf,user_sports_inf,user_music_inf,user_movies_inf,
                 user_tv_inf,user_books_inf,user_likes_inf,user_reviews_inf,user_posts_inf)]

    #print(10)
    write_to_sql(user_data)
    #print('check_4')


def get_user_about(browser,part_1,part_2,part_3):
    browser.get(part_1 + part_2 + part_3)
    

    elements_in_about = browser.find_elements_by_class_name('_5pws')

    about_user_list = []
    
    #work_and_education__tab.click()
    
    for i in range(1,7):
        elements_in_about[i].click()
        about_user_list.append(browser.find_element_by_class_name('_4ms4').text)
        time.sleep(1)

    return about_user_list

    
        
def get_user_more(browser,part_1,part_2,part_3):
    #print(part_1 , part_2 , part_3)
    try:
        browser.get(part_1 + part_2 + part_3)
    
        return browser.find_element_by_class_name('_3i9').text
    except:
        return "No information"


def scroll_page(browser, max_scroll_count,scroll_pause_time):

    scrolls_count = 1
        
    while True:
            
        if scrolls_count == max_scroll_count:
            break
                    
        try:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
                        
            last_height = new_height
    
        except:
            pass
        
        scrolls_count+=1
        time.sleep(scroll_pause_time)



def get_all_user_posts(browser):
    user_posts_text = "Старт"
    all_posts = browser.find_elements_by_class_name('_4-u2')
    
    for i in all_posts:
        try:
            user_posts_text = user_posts_text + "Пост" + i.text 
            
        except:
            pass
    
    return user_posts_text



def write_to_sql(list_of_user_data):
    conn = sqlite3.connect('Книгой_по_лицу_data.db')
    c = conn.cursor()   

    c.executemany('INSERT INTO user_info VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', list_of_user_data)
    conn.commit()
    



def watch_acc_feed(browser, duration):
    
    start_value = 500
    time_start = time.time()

    duration = duration + random.randint(1,150)
    
    links = ['https://www.facebook.com/groups/401816383615230/',
             'https://www.facebook.com/groups/843804142348443/',
             'https://www.facebook.com/groups/457761797950055/',
             'https://www.facebook.com/groups/ProgramersCreateLife/',
             'https://www.facebook.com/groups/154723298501253/',
             'https://www.facebook.com/music.dance20/',
             'https://www.facebook.com/CaravanPalace/',
             'https://www.facebook.com/smashmouth/',
             'https://www.facebook.com/groups/612291468916490/',
             'https://www.facebook.com/groups/153558955177570/']
    
    browser.get(links[random.randint(0,3)])
    while True:
          #Generate the random length of news feed scrolling 
          browser.execute_script("window.scrollTo(0, %s)" % random.randint(start_value, start_value + 1000)) 


          like_buttons = browser.find_elements_by_class_name('UFILikeLink')
          #print("Like buttons count: ",len(like_buttons))

        
          like_buttons_count = len(like_buttons)

          random_like = random.randint(1,like_buttons_count-1) #Доработать алгоритм
          like_button = like_buttons[random_like] 

        
          chance = random.randint(1,100)
          #print(chance,"%")
          if chance <= 10:
               try:
                    like_button.click()
                    print("Liked successfully")
               except:
                    print("Isn't liked")
        
        
          start_value += 1000
        
          
        
          time.sleep(1)
          
          if time.time() >= time_start + duration:
              break
          


          




if __name__ == '__main__':
    main()
