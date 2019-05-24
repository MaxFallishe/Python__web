import requests
import getpass
import json

username = "MaxFallishe"
password = "Bvad13nik"

data = requests.get('https://api.github.com/user/repos',auth=(username, password))

jobs = json.loads(data.text)

count = 0

with open('log.txt','w+',encoding = 'utf-8') as lfile:
    lfile.write('Repositories: ')
    try:
        while True:
            lfile.write(jobs[count]['name']+', ')
            count += 1
    except:
       lfile.close() 
    




#Что означает [0], и что от от него зависит? Можно ли было сделать проще?
