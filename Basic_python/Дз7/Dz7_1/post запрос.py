import requests
import getpass

user = 'MaxFallishe'
message = getpass.getpass('Message: ')

r = requests.post('https://api.github.com/user',data = {'user':user,'message':message})

print(r)

