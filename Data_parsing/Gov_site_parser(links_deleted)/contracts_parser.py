import requests
from bs4 import BeautifulSoup
import urllib3
import time
import xlwt
import csv




book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
excel_string_num = 0


def main():
    warnings_off()
    with open("BINs.txt") as file:
        for line in file.readlines():
            contractor_name = line.split('--')[0]
            contractor_bin = line.split('--')[1]
            print(contractor_name, contractor_bin)
            ready_url = generate_url(contractor_bin)
            pages_count = get_pages_count(ready_url)
            parsing_data(pages_count, ready_url)


def warnings_off():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # switch off the warning


def generate_url(bin):
    basis_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    contractor_bin = bin  # "921027301248"
    first_date = "01.10.2018"
    second_date = "30.03.2019"

    ready_url = basis_url.replace("BIN", contractor_bin).replace("FIRSTDATE", first_date).replace("SECONDDATE", second_date)
    print(ready_url)
    return ready_url


def get_pages_count(url):
    one_page_exception = "javascript:void(0)"

    r = requests.get(url, verify=False)  # don't forget about verify=False (if site don't have https
    soup = BeautifulSoup(r.text, features="html.parser")

    pages_count = soup.find('div', class_='col-md-6 text-center').find_all('li')[-1].find('a').get('href')

    if pages_count != one_page_exception:
        pages_count = pages_count.split('page=')
        # print(pages_count[-1])
        return int(pages_count[-1])
    else:
        return 1


def parsing_data(pages_count, url):
    global excel_string_num
    if pages_count == 0:
        print("No result with this BIN")
    else:
        for i in range(1, pages_count + 1):
            r = requests.get(url + "&page=" + str(i), verify=False)
            soup = BeautifulSoup(r.text, features="html.parser")
            link_list = soup.find_all('div', class_='panel panel-white')[-1]\
                .find('div', class_='panel-body')\
                .find('table')\
                .find('tbody')\
                .find_all('tr')

            for j in link_list:
                attributes = j.find_all('td')
                contract_number = attributes[1].text
                purchase_method = attributes[-1].text
                contractor_name = attributes[-2].text
                customer = attributes[-3].text
                contract_href = attributes[1].find('a').get('href').replace('show', 'units')
                # print(contract_number)
                print(contract_href)
                try:
                    r2 = requests.get(contract_href, verify=False)
                    soup2 = BeautifulSoup(r2.text, features="html.parser")
                    items = soup2.find('table').find_all('tr')[1:]
                except Exception as e:
                    print(e)
                    print(soup2)
                # print(soup2)

                for k in items:
                    item_attributes = k.find_all('td')
                    summ = item_attributes[-1].text
                    unit_price = item_attributes[-2].text
                    amount = item_attributes[-4].text
                    name = item_attributes[-5].text
                    if "Герб" in name or "герб" in name:
                        print(summ)
                        print(unit_price)
                        print(amount)
                        print(name)  # здесь закончил
                        print('----------------------------------------')
                        sheet1.write(excel_string_num, 0, contract_number)
                        sheet1.write(excel_string_num, 1, customer)
                        sheet1.write(excel_string_num, 2, contractor_name)
                        sheet1.write(excel_string_num, 3, name)
                        sheet1.write(excel_string_num, 4, amount)
                        sheet1.write(excel_string_num, 5, unit_price)
                        sheet1.write(excel_string_num, 6, summ)
                        sheet1.write(excel_string_num, 7, purchase_method)
                        book.save("Table_data2018.xls")
                        excel_string_num = excel_string_num + 1


                    else:
                        print(name, " *does not fit")
                        print('----------------------------------------')
                    time.sleep(2)


            # print(soup)
            print(len(link_list))


if __name__ == '__main__':
    main()
