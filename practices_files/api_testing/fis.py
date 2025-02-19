import requests
import json

# API Endpoint
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
response= response.json()
print(response['bpi'])
currency_set=['USD','GBP','EUrr']
print(type(currency_set))

assert response['bpi'][i]['code'] in currency_set:
        break
    else:
        print('failed')
