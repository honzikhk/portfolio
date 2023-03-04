from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def get_all_coin_and_information():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        #'limit':'50',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '2f38cdc8-46d7-4b2d-9a08-e978a97d247a',        # hide this
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        #print(e)
        return e
    

data_for_json = json.dumps(get_all_coin_and_information())

with open("all_data.json", "w") as outfile:
    outfile.write(data_for_json)
