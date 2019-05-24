import sqlite3
import time
from selenium import webdriver

url = "https://business.gov.kz/ru/directory-of-companies/?PAGEN_2="
start_page = 1


def main():
    browser = webdriver.Chrome('chromedriver.exe')
    browser.maximize_window()
    infinitive_scrapping(browser, start_page)


def infinitive_scrapping(browser, page_number):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    while True:
        try:
            browser.get(url + str(page_number))
            list_of_companies = browser.find_elements_by_class_name('expert_block')
            print(page_number)
            for i in list_of_companies:
                print(i.find_element_by_tag_name('a').get_attribute("href"))
                link = i.find_element_by_tag_name('a').get_attribute("href")
                c.execute('''INSERT INTO companies_links (url) VALUES (?)''', (link,))
                conn.commit()
            page_number += 1
        except:
            break

    print('end, analyze the ', page_number, ' pages')


if __name__ == '__main__':
    main()