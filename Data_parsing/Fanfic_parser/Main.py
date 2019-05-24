import requests
from bs4 import BeautifulSoup


page_url = "http://fanfics.me/fandom2?action=fics&p=on&page="
api_url = "http://fanfics.me/api.php"


for i in range(1, 900+1):
    print("Page№ ", i)
    r = requests.get(page_url + str(i) + "#fics")
    soup = BeautifulSoup(r.text, features="html.parser")

    fanfics_id = soup.find_all('div', class_='FicTable')

    for j in fanfics_id:
        fanfic = j.find('a')
        print(fanfic)
        fanfic_link = fanfic.get('href')

        with open('product_links.txt', 'a') as file:
            file.write("http://fanfics.me" + fanfic_link + '\n')
