from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from decouple import config
import json

my = {'Bitcoin': 1, 'CasinoCoin': 45, 'ethereum': 1027}

# print(type(my))
# for k, v in my.items():
#     print(f"key: {k}, value: {v}")
v = "1"

def find_price(id_of_coin):

    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'       # link for price. must contain id,slug or symbol
    parameters = {
        "id":id_of_coin,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config("X-CMC_PRO_API_KEY"),        # the key is in .env file
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price =  data["data"][v]["quote"]["USD"]["price"]
        return price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
