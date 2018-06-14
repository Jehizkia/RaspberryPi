import pymssql
import time
import logging

logging.basicConfig(level=logging.INFO)

server = 'ictlab1.database.windows.net'
user = 'ictlab@ictlab1'
password = 'Henkie123'
database = 'dashboard_db_Copy'

try:
    conn = pymssql.connect(server=server, user=user, password=password, database=database)
    cursor = conn.cursor()
except Exeption as e:
    print('An error has occured: {}'.format(e))

def getAll(table):
    try:
        cursor.execute('SELECT * FROM {}'.format(table))
        row = cursor.fetchall()
    except Exception as e:
        print ('An error has occured: {}'.format(e)) 
    print row

def getById(table, itemID):
    try:
        logging.info('Get {} by {}'.format(table, itemID))
        cursor.execute('SELECT * FROM {} WHERE id = {}'.format(table, itemID))
        row = cursor.fetchall()
    except Exception as e:
        logging.ERROR('Error getBYID has occured : {}'.format(e))
    return row

def getBy(table, column, item):
    try:
        logging.info('Get {} by {} = {}'.format(table, column, item))
        cursor.execute('SELECT * FROM {} WHERE {} = {}'.format(table, column, item))
        row = cursor.fetchall()
    except Exception as e:
        print('Error getBY has occured : {}'.format(e))
    return row                    


def getRaspberryByRoom(room_code):
    try:
         logging.info('Get Raspberry from: {} '.format(room_code))
         query = "SELECT * FROM Raspberry WHERE room_code = '{}'".format(room_code)
         cursor.execute(query)
         row = cursor.fetchall()
    except Exception as e:
         logging.ERROR('Error getBYID has occured : {}'.format(e))
    return row

def insertRaspberry(room_code,active=1):
    try:
        query = "INSERT INTO Raspberry (active, room_code) VALUES (0, '{}')".format(room_code)
        cursor.execute(query)
        conn.commit()
        logging.info('Row inserted: {}'.format(room_code))
    except Exception as e:
        logging.ERROR('Error getBYID has occured : {}'.format(e))


def insertTempHum(temp, hum, room_code, timestamp):
    try:
        query = "INSERT INTO TemperatureHumidity (temperature, humidity, room_code, timestamp) VALUES ({},{},'{}', {})".format(temp, hum, room_code, timestamp)
        cursor.execute(query)
        conn.commit()
        logging.info('Sensor data inserted into: {}'.format(room_code))
    except Exception as e:
        print ('An error has occured: {}'.format(e))


def updateRaspberry(rpiID, room_code):
    try:
        query = "UPDATE Raspberry SET room_code='{}' WHERE id={}".format(room_code, rpiID) 
        cursor.execute(query)
        conn.commit()
        logging.info('Room {} updated: {}'.format(rpiID,room_code))
    except Exception as e:
        print ('An error has occured: {}'.format(e))


def sendData():
    print 'Sending to server'
