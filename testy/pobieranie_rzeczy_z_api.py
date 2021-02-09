import requests

respond = requests.get("https://randomuser.me/api?results=10")

date = respond.json()

for resultsy in date['results']:
    name = resultsy['name']
    if name['title'] == 'Mr':
        print("{} {} {} and his phone number: {}".format(name['title'], name['first'], name['last'], resultsy['phone']))
    else:
        print("{} {} {} and her phone number: {}".format(name['title'], name['first'], name['last'], resultsy['phone']))
    