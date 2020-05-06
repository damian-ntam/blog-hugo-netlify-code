
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=percent_change_24h&limit=10'
#url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=percent_change_24h&limit=10'


#headers_sandbox = {
#  'Accept': 'application/json',
#  'X-CMC_PRO_API_KEY': '258de408-dad2-429b-af8e-f6350a992614',
#}

headers = {
  'Accept': 'application/json',
  'X-CMC_PRO_API_KEY': '6044309f-c086-420e-83fd-7a4b27e0fdae',
}


session = Session()
session.headers.update(headers)

try:
  response = session.get(url).json()
  #data = json.loads(response.text)
  data = response['data']
  for currency in data:
    print(f"{currency['cmc_rank']} => {currency['name']}")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)