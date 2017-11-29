#This code is simulating writing 1 million data points to and reading them from MySql database
import datetime
from datetime import timedelta
import sys
import random
import MySQLdb

#Create connection to MySQL database
conn = MySQLdb.connect(host= "localhost",user="root",passwd="admin",db="rainfallcase2")
session = conn.cursor()

#Define variables
max_column = 550
max_row = 500
dt = datetime.datetime.strptime("2016-01-01T00:00:00.000", "%Y-%m-%dT%H:%M:%S.%f")
column = 1
row = 1
counter = 1

#Set current datetime before execution
currdatetimebeforeexecution = datetime.datetime.now()
# Simulate writing 100000 data points
for i in range (0,1000000):
    rain_mm = random.randint(15,60)
    try:
       session.execute("""INSERT into image (timestamp,X,Y,amount) values(%s,%s,%s,%s)""",(dt,column,row,rain_mm))
       conn.commit()

       column = column+1
       counter = counter+1
       if (column > 53):
           column = 1
           row = row + 1
       if (row > 50):
           row = 1
       if (counter > 1000):
           counter = 1
           dt = dt + datetime.timedelta(minutes = 5)
    except:
       e = sys.exc_info()
       print("insert error ", e)


results = None
#Simulate reading one image
try:
    session.execute("select * from image where timestamp='%s'"% (dt))
    results = session.fetchall()
except:
    e = sys.exc_info()
    print("select error: ", e)

#Simulate reading based on x and y location
try:
    session.execute("Select * from image where X=1 and Y=1")
    results = session.fetchall()
except:
    e = sys.exc_info()
    print("select error: ", e)

#Set current datetime before execution
currdatetimeafterexecution = datetime.datetime.now()

#Calculate delta beween datetime before and after execution
time_difference = currdatetimeafterexecution - currdatetimebeforeexecution
time_difference_in_seconds = time_difference.total_seconds()
print("Time difference in seconds ", time_difference_in_seconds)

#Print the actual datetime before and after execution
print(currdatetimeafterexecution)
print(currdatetimebeforeexecution)
