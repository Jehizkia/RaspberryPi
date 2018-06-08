import pymssql
import time

server = 'ictlab1.database.windows.net'
user = 'ictlab@ictlab1'
password = 'Henkie123'
database = 'dashboard_db_Copy'

conn = pymssql.connect(server=server, user=user, password=password, database=database)
cursor = conn.cursor()

def getAll(table):
    try:
        cursor.execute('SELECT * FROM {}'.format(table))
        row = cursor.fetchall()
    except Exception as e:
        print ('An error has occured: {}'.format(e)) 
    print row

def getById(table, itemID):
    try:
        cursor.execute('SELECT * FROM {} WHERE id = {}'.format(table, itemID))
        row = cursor.fetchall()
    except Exception as e:
        print ('An error has occured: {}'.format(e))
    return row

def getBy(table, column, item):
    try:
        cursor.execute('SELECT * FROM {} WHERE {} = {}'.format(table, column, item))
        row = cursor.fetchall()
    except Exception as e:
        print ('Error: {}'.format(e))
    return row                    

def insertRaspberry(room_code,active=1,):
    try:
        cursor.execute('INSERT INTO Raspberry (active, room_code) VALUES({},{})'.format(active, room_code))
        conn.commit()
    except Exception as e:
        print ('An error has occured: {}'.format(e))


def insertTempHum(temp, hum, room_code, timestamp):
    try:
        cursor.execute('INSERT INTO TemperatureHumidity (temperature, humidity, room_code, timestamp) VALUES ({},{},{}, {})'.format(temp, hum, room_code, timestamp))
        print ('Inserted')
    except Exception as e:
        print ('An error has occured: {}'.format(e))


def sendData():
    print 'Sending to server'

#insertTempHum(24.4,56.4,25, int(time.time()))
#insertRaspberry(25)
#getAll('TemperatureHumidity')


