#imports
import requests
import configHandler as config
import logging
import time
import json

logging.basicConfig(level=logging.INFO)

apiUrl = config.getData('app_data', 'api_url')


def createUrl(route):
    return apiUrl + route

def getData(route, urlParameters=''):
    try:
        logging.info('Getting data from: {}'.format(route))
        response = requests.get(createUrl(route), params=urlParameters)
        logging.info('Status code request: {}'.format(response.status_code))
        return response.text

    except requests.exceptions.RequestException as e:
        logging.error(e)


def postData(route, payload):
    try:
        logging.info('Post data to : {}'.format(route))
        headers = {'Content-Type': 'application/json'}
        response = requests.post(createUrl(route), json=payload)
        logging.debug(response)
        logging.info('done')
    except requests.exceptions.RequestException as e:
        logging.error(e)

#print getData('/rpi/get/room/H.1.110')

#data = {'temperature': 11.1,'humidity': 11.1, 'timestamp': time.time(), 'room_code': 'H.1.110'}

#postData('/rpi/add/sensorData', data)
