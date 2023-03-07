from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from decouple import config

def get_all_coins_and_informations():
    """
    take data from coinmarketcap and return it. In case of fail, raise error. The parameter "limit" sets how many coin will be in json
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        'limit':'50',
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
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e


def write_all_data_to_json_file():
    """
    take returned data from function "get_all_coins_and_informations" and rewrite the all_data.json file
    """
    data_for_json = json.dumps(get_all_coins_and_informations())

    with open("all_data.json", "w") as outfile:
        outfile.write(data_for_json)


def extract_price(list_of_coins):
    for coin in list_of_coins:
        for name in all_data.json:
            if coin.lower() == name:
                pass