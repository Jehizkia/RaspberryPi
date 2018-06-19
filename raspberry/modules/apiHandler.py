#imports
import requests
from configHandler import Configuration as config
import logging
import time
import json

logging.basicConfig(level=logging.INFO)

class ApiRequest():
    
    def __init__(self):
        self.apiUrl = config().getData('app_data', 'api_url')

    def createUrl(self, route):
        return self.apiUrl + route

    def getData(self, route, urlParameters=''):
        try:
            logging.info('Getting data from: {}'.format(route))
            response = requests.get(self.createUrl(route), params=urlParameters, timeout=30)
            logging.info('Status code request: {}'.format(response.status_code))
            return response.text

        except requests.exceptions.RequestException as e:
            logging.error(e)

    def postData(self, route, payload):
        try:
            logging.info('Post data to : {}'.format(route))
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.createUrl(route), json=payload)
            logging.debug(response)
            logging.info('done')
        except requests.exceptions.RequestException as e:
            logging.error(e)
