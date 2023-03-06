"""
only backup, can be deleted later
"""


from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from decouple import config

def get_all_coins_and_informations_to_json_file():
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


data_for_json = json.dumps(get_all_coins_and_informations_to_json_file())

with open("all_data.json", "w") as outfile:
    outfile.write(data_for_json)
