#imports
import requests
import configHandler as config

apiUrl = config.getData('app_data', 'api_url')

# GET request
def getData(route,payload):
    try:
        print('-[Request]> Get data')
        url = apiUrl + route
        r = requests.get(url, params=payload)
        print('-[Response]> Status code: %s' % r.status_code)
        return r.text

    except requests.exceptions.RequestException as e:
        print(e)

# POST request

pay = {}
url = ''

print(getData(url,pay))
