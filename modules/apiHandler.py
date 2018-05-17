#imports
import requests

apiUrl = 'http://192.168.43.194:3000/'

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

# POST request k

pay = {}
url = ''

print(getData(url,pay))
