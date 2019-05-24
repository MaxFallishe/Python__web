import sqlite3
import time
from selenium import webdriver
#Select column_name from table_name where id = ??? ;


def main():
    browser = webdriver.Chrome('chromedriver.exe')
    browser.maximize_window()

    conn = sqlite3.connect('database(new).db')
    c = conn.cursor()
    all_links = c.execute('SELECT * FROM companies_links')

    for link in all_links:
        time.sleep(1)
        browser.get(link[0])
        all_info = browser.find_element_by_class_name('table-zakupki-4-wrap').find_elements_by_tag_name('tr')

        print(link[0])
        name = browser.find_element_by_class_name('sub_cont').find_element_by_tag_name('h1').text
        email = 'не указано'
        www_adress = 'не указано'
        adress = 'не указано'
        additional = 'не указано'
        locality = 'не указано'
        legal_form = 'не указано'
        post_index = 'не указано'
        phone = 'не указано'
        activity = 'не указано'

        try:
            for i in all_info:
                filling = i.find_elements_by_tag_name('td')
                category_name = filling[0].text
                category_text = filling[1].text

                if category_name == 'E-mail:':
                    email = category_text
                elif category_name == 'WWW-адрес:':
                    www_adress = category_text
                elif category_name == 'Адрес:':
                    adress = category_text
                elif category_name == 'Доп. информация:':
                    additional = category_text
                elif category_name == 'Населенный пункт:':
                    locality = category_text
                elif category_name == 'Орг.-правовая форма:':
                    legal_form = category_text
                elif category_name == 'Почтовый индекс:':
                    post_index = category_text
                elif category_name == 'Телефон:':
                    phone = category_text
                elif category_name == 'Товары и услуги:':
                    activity = category_text
                else:
                    pass
                #print([(email, www_adress, adress, additional, locality, legal_form, post_index, phone, activity)])


            #conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.executemany('INSERT INTO Companies_full_info VALUES (?,?,?,?,?,?,?,?,?,?)', [(name, email, www_adress, adress, additional, locality, legal_form, post_index, phone, activity)])
            conn.commit()
        except:
            pass


if __name__ == '__main__':
    main()
