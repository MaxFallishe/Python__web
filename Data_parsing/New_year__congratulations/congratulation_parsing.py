import requests
from bs4 import BeautifulSoup
import time








def main():
    
    for i in range(1,200+1):
        try:
            url = "http://pozdravok.ru/pozdravleniya/prazdniki/noviy-god/"+ str(i) +".htm"

            response = requests.get(url)
            html = response.content

            soup = BeautifulSoup(html, "html.parser")


            lyrics = soup.find('div',class_ = 'content').find_all('p', class_ ='sfst')

            #print(url)
            for verse in lyrics:
                print('*')
                print(verse.text)

        except:
            pass
            
            


        
        

        

        

        
    
    



if __name__ == '__main__':
    main()
