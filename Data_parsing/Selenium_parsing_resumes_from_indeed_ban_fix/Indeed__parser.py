from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import xlwt




def main():     #programm start from here

    global book
    global sheet1
    global x
    global browser

    browser = webdriver.Chrome("D:\\Selenium\\Chrome\\chromedriver.exe")
    browser.maximize_window()
    x = 1
    url = 'https://www.indeed.com/resumes?q=Pharmacist&l=US&start=250' 
    browser.get(url)

    sign_in_button = browser.find_element_by_id('signInFromBanner')
    sign_in_button.click()


    email = browser.find_element_by_id('signin_email')
    email.send_keys('n13b@inbox.ru')

    password = browser.find_element_by_id('signin_password')
    password.send_keys('Bvad13nik')

    button = browser.find_element_by_xpath('//*[@id="loginform"]/button')
    button.click()




        
    #url = 'https://www.indeed.com/resumes?q=Dentist&co=US&start=0'  - example of url

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
        
    sheet1.write(0, 0 , "Profession")
    sheet1.write(0, 1 , "Location")
    sheet1.write(0, 2 , "Experience (in short)")
    sheet1.write(0, 3 , "Education(in short)")
    sheet1.write(0, 4 , "Account link(in short)")
    sheet1.write(0, 5 , "Work expirience")
    sheet1.write(0, 6 , "Education" )
    sheet1.write(0, 7 , "Skills")
    sheet1.write(0, 8 , "Additional information")

    

    book.save("Resumes_Selenium_try_to_parse_more_resumes(part1_new_except).xls")

    
    generate_url()
    launch_fake_google()


def generate_url():
    
    arr_of_jobs = ['Pharmacy+Technician', 'Construction+Manager', 'Public+Relations+Specialist', 'Middle+School+Teacher', 'Massage+Therapist', 'Paramedic', 'Preschool+Teacher', 'Hairdresser', 'Marketing+Manager', 'Patrol+Officer', 'School+Counselor', 'Executive+Assistant', 'Financial+Analyst', 'Personal+Care+Aide', 'Clinical+Social+Worker', 'Business+Operations+Manager', 'Loan+Officer', 'Meeting,+Convention+&+Event+Planner', 'Mental+Health+Counselor', 'Nursing+Aide', 'Sales+Representative', 'Architect', 'Sales+Manager', 'HR+Specialist', 'Plumber', 'Real+Estate+Agent', 'Glazier', 'Art+Director', 'Customer+Service+Representative', 'Logistician', 'Auto+Mechanic', 'Bus+Driver', 'Restaurant+Cook', 'Child+&+Family+Social+Worker', 'Administrative+Assistant', 'Receptionist', 'Paralegal', 'Cement+Mason+&+Concrete+Finisher', 'Painter', 'Sports+Coach', 'Teacher+Assistant', 'Brickmason+&+Blockmason', 'Cashier', 'Janitor', 'Electrician', 'Delivery+Truck+Driver', 'Maid+&+Housekeeper', 'Carpenter', 'Security+Guard', 'Construction+Worker', 'Fabricator', 'Telemarketer']


    for arr in arr_of_jobs:
        generate_url_2(arr)


def generate_url_2(arr):
    
    for num in range (250,2050,50):     # in last fix add this except
        #time.sleep(2000)
        try:
            generate_url_3(arr, num)

        except:
            time.sleep(2)
            continue
    
        

   
def generate_url_3(arr, num):

    global gap_url_p2
    
    gap_url_p1 = 'https://www.indeed.com/resumes?q='
    gap_url_p2 = arr
    gap_url_p3 = '&l=US&start='
    gap_url_p4 = num #0, 50, 100, 150  

    gap_F = gap_url_p1 + gap_url_p2 + gap_url_p3 + str(gap_url_p4)
    
    print(gap_F)
    print('|--------------------------------------|')
    
    launch_fake_google(gap_F)
    


def launch_fake_google(gap_F):


    print('Start Program')

    
    global browser
    
    browser.get(gap_F)
    all_vac_on_page = browser.find_elements_by_class_name('sre')
    #time.sleep(3)   #delay can be changed


    first_vac_treatment(all_vac_on_page)
    #authorization_in_indeed(browser)



def first_vac_treatment(all_vac_on_page):  
    global book
    global sheet1
    global x
    global gap_url_p2
    

    for vac_content in all_vac_on_page:
        
        try:
            #_name = vac_content.find_element_by_class_name('app_name').find_element_by_class_name('app_link').text
            _name = gap_url_p2
            
        except:
            _name = 'Not indicated'


        try:
            _location = vac_content.find_element_by_class_name('app_name').find_element_by_class_name('location').text

        except:
            _location = 'Not indicated'

        try:
            _experience = vac_content.find_elements_by_class_name('experience')
            _jobs = ''

            for _exp in _experience:
                    
                try:  
                    _jobs = _jobs + _exp.text + ', '

                except:
                    pass
                
        except:
            _jobs = ''
                


        try:
            _education = vac_content.find_element_by_class_name('education').text

        except:
            _education = ''
        

        try:
            
            _account_link = vac_content.find_element_by_class_name('app_name').find_element_by_class_name('app_link').get_attribute("href")
            #print(_account_link)
        except:
            pass

        
        hover = ActionChains(browser).move_to_element(vac_content)
        hover.perform()

        preview = browser.find_element_by_class_name('preview').find_element_by_class_name('resume_content')

        exp = preview.text

        _resume_workexp = 'Not indicated' 
        _resume_education = 'Not indicated'
        _resume_skills = 'Not indicated'
        _resume_addinf = 'Not indicated' 
        
        try:
            exp = exp.split('Дополнительная информация')
            _resume_addinf = exp[1]

            exp = exp[0].split('Навыки')
            _resume_skills = exp[1]

            exp = exp[0].split('Образование')
            _resume_education = exp[1]

            exp = exp[0].split('Опыт работы')
            _resume_workexp = exp[1]
            
        except:
            try:
                exp = exp[0].split('Навыки')
                _resume_skills = exp[1]
        
                exp = exp[0].split('Образование')
                _resume_education = exp[1]

                exp = exp[0].split('Опыт работы')
                _resume_workexp = exp[1]
                
            except:
                try:
                    exp = exp[0].split('Образование')
                    _resume_education = exp[1]

                    exp = exp[0].split('Опыт работы')
                    _resume_workexp = exp[1]

                except:
                    try:
                        exp = exp[0].split('Опыт работы')
                        _resume_workexp = exp[1]
                        
                    except:
                        pass

        

        
        
        



        
        #print('Name:', _name)
        #print('|------------------------------------------------------------------------|')

        data = {'_name':_name,
                '_location':_location,
                '_jobs':_jobs,
                '_education':_education,
                '_account_link':_account_link,
                '_resume_workexp':_resume_workexp,
                '_resume_education':_resume_education,
                '_resume_skills':_resume_skills,
                '_resume_addinf':_resume_addinf}
        
        sheet1.write(x, 0,  data['_name'])
        sheet1.write(x, 1,  data['_location'])
        sheet1.write(x, 2,  data['_jobs'])
        sheet1.write(x, 3,  data['_education'])
        sheet1.write(x, 4,  data['_account_link'])
        sheet1.write(x, 5 , data['_resume_workexp'])
        sheet1.write(x, 6 , data['_resume_education'])
        sheet1.write(x, 7 , data['_resume_skills'])
        sheet1.write(x, 8 , data['_resume_addinf'])
        
        book.save("Resumes_Selenium_try_to_parse_more_resumes(part1_new_except).xls") #xls #csv
        

        x = x + 1

        


        
        
        
        

def authorization_in_indeed(browser):
    email = browser.find_element_by_id('signin_email')
    email.send_keys('n13b@inbox.ru')

    password = browser.find_element_by_id('signin_password')
    password.send_keys('Bvad13nik')

    button = browser.find_element_by_xpath('//*[@id="loginform"]/button')
    button.click()

    time.sleep(3)   #delay can be changed

    



         




if __name__ == '__main__':
    main()









    
