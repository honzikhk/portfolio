from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from decouple import config
import json

my = {'Bitcoin': 1, 'CasinoCoin': 45, 'ethereum': 1027}

# print(type(my))
# for k, v in my.items():
#     print(f"key: {k}, value: {v}")
v = "1"

def find_prices():


        url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'       # link for price. must contain id,slug or symbol
        parameters = {
            "id":v,
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
            price =  data["data"]["quote"]["USD"]["price"]
            return price
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

#print(find_prices())

j = {
"data": {
"1": {
"id": 1,
"name": "Bitcoin",
"symbol": "BTC",
"slug": "bitcoin",
"is_active": 1,
"is_fiat": 0,
"circulating_supply": 17199862,
"total_supply": 17199862,
"max_supply": 21000000,
"date_added": "2013-04-28T00:00:00.000Z",
"num_market_pairs": 331,
"cmc_rank": 1,
"last_updated": "2018-08-09T21:56:28.000Z",
"tags": ["mineable"],
"platform": None,
"self_reported_circulating_supply": None,
"self_reported_market_cap": None,
"quote":
    {"USD":
        {
            "price": 6602.60701122,
"volume_24h": 4314444687.5194,
"volume_change_24h": -0.152774,
"percent_change_1h": 0.988615,
"percent_change_24h": 4.37185,
"percent_change_7d": -12.1352,
"percent_change_30d": -12.1352,
"market_cap": 852164659250.2758,
"market_cap_dominance": 51,
"fully_diluted_market_cap": 952835089431.14,
"last_updated": "2018-08-09T21:56:28.000Z"}}}},
"status": {
"timestamp": "2023-03-08T01:07:46.478Z",
"error_code": 0,
"error_message": "",
"elapsed": 10,
"credit_count": 1
}
}

print(j["data"][v]["quote"]["USD"]["price"])