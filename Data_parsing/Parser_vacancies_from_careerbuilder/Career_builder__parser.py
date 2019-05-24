import requests
from bs4 import BeautifulSoup
import csv
import xlwt

#Выясеить кол-во страниц
#Cформировать список url на странице выдачи
#Собрать данные
#Загрузить в csv



def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')    
    pages = soup.find('div',class_='row bump pagination').find('a',class_ = 'btn tertiary pagination-btn last').get('href')
    total_pages = pages.split('=')[1]

    return int(total_pages)
    #return 12

def pred_get_page_data(html):
    try:
        soup = BeautifulSoup (html, 'lxml')
        ads = soup.find('div', class_= 'jobs').find_all('div', class_ = 'job-row')
        get_page_data(html, ads)
    except:
        print('Err 404')


def get_page_data(html,ads):
    global job_type

    

    base_url_2 = 'https://www.careerbuilder.com'

    for ad in ads:
        #vacancy_name, vacancy_company_name, adress, pay, type of work 
        
        try:            
            vacancy_name = ad.find('div',class_ = 'row').find('h2',class_ = 'job-title show-for-medium-up').find('a').text                 
                       
        except:            
            try:
                vacancy_name = ad.find_all('div',class_ = 'row')[1].find('div',class_ = 'column small-10').find('h2',class_ ='job-title hide-for-medium-up').text.strip()

            except:
                #print(ad)
                continue
    
        try:
            vacancy_company_name = ad.find('div',class_ = 'row job-information').find('div', class_='columns large-2 medium-3 small-12').find('a').text

        except:
            try:
                vacancy_company_name = ad.find('div',class_ = 'row job-information').find('div', class_='columns large-2 medium-3 small-12').find('h4', class_ = 'job-text').text.strip()

            except:
                continue

        try:
            address = ad.find('div',class_ = 'row job-information').find('div',class_ = 'columns end large-2 medium-3 small-12').find('h4', class_ = 'job-text').text.strip()

        except:
            continue
            
        try:
            employment_and_pay = ad.find('div',class_ = 'row job-information').find('div', class_ = 'columns medium-6 large-8').find('h4',class_ = 'job-text employment-info').text.strip()
            employment_and_pay = employment_and_pay.split('|')
            employment = employment_and_pay[0]
                
            try:
                pay = employment_and_pay[1]
                pay = pay.replace(',', '.')
                
            except:
                pay = 'Not specified ' 
            
        except:
            continue

        try: 
            destination_link = ad.find('div',class_ = 'row').find('div',class_ = 'column small-10').find('h2',class_ ='job-title hide-for-medium-up').find('a').get('href') 
            url_2 = base_url_2 + destination_link
            print(url_2)
            r = requests.get(url_2)
            soup_large = BeautifulSoup(r.text, 'lxml')
            
            job_d = " "
            job_r = " "
            job_d = soup_large.find('div', class_ = 'small-12 columns item').text.strip()

            try:
                job_d = job_d.strip('Job Description')

            except:
                pass
                        
            
            
        except:
            try:
                destination_link = ad.find_all('div',class_ = 'row')[1].find('div',class_ = 'column small-10').find('h2',class_ ='job-title hide-for-medium-up').find('a').get('href')
                url_2 = base_url_2 + destination_link
                print(url_2)
                r = requests.get(url_2)
                soup_large = BeautifulSoup(r.text, 'lxml')
                job_d = ''
                job_r = ''
                job_d = soup_large.find('div', class_ = 'small-12 columns item').text.strip()
                try:
                    job_d = job_d.strip('Job Description')
                    
                except:
                    pass
                
            except:
                continue
                
                    

        

        data = {'search_query_on_the_site':job_type,
                'vacancy_name':vacancy_name,
                'vacancy_company_name':vacancy_company_name,
                'address':address,
                'employment':employment,
                'pay':pay,
                'job_d':job_d #description
                    }
        #print(data)
        print('|-------------------------------------------------------------------------|')
        write_csv(data)
        


def write_csv(data):
    global book
    global sheet1
    global x
    
    sheet1.write(x, 0, data['search_query_on_the_site'])
    sheet1.write(x, 1, data['vacancy_name'])
    sheet1.write(x, 2, data['vacancy_company_name'])
    sheet1.write(x, 3, data['address'])
    sheet1.write(x, 4, data['employment'])
    sheet1.write(x, 5, data['pay'])
    sheet1.write(x, 6, data['job_d'])

    book.save("Tabel_with_new_vacancies(2).xls") #xls #csv

    x = x + 1 

    
        

def main():
    global book
    global sheet1
    global job_type
    global x

    arr_of_jobs = ['here']
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
        
    sheet1.write(0, 0, "Search query on the site")
    sheet1.write(0, 1, "Job title")
    sheet1.write(0, 2, "Company name")
    sheet1.write(0, 3, "Address of work place")
    sheet1.write(0, 4, "Employment")
    sheet1.write(0, 5, "Pay")
    sheet1.write(0, 6, "Job description")
        
    

    x = 1
    for elm in arr_of_jobs:

        
        url= 'https://www.careerbuilder.com/jobs-software-developer?page_number=1'
        base_url = 'https://www.careerbuilder.com/'
        job_type = elm # be changed
        page_part = '?'
        query_part = 'page_number='


        total_pages=get_total_pages(get_html(url))
       
        for i in range (1, total_pages+1):
           
            url_gen = base_url + job_type + page_part  + query_part + str(i)
            print(url_gen)
            html = get_html(url_gen)
            pred_get_page_data(html)        ######
        
    

if __name__ == '__main__':
    main()
