#This code is simulating writing 1 million data points to and reading them from cassandra database

import datetime
from datetime import timedelta
import sys
import random
from cassandra.cluster import Cluster

#Create connection to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('rainfallcase2')

#Define variables
max_column = 550
max_row = 500
dt = datetime.datetime.strptime("2016-01-01T00:00:00.000", "%Y-%m-%dT%H:%M:%S.%f")
column = 1
row = 1
counter = 1

#Set current datetime before execution
currdatetimebeforeexecution = datetime.datetime.now()
# Simulate writing 1 million data points
for i in range (0,1000000):
    rain_mm = random.randint(15,60)
    try:
       session.execute("""INSERT INTO image (timestamp,x,y,amount) VALUES (%s,%s,%s,%s)""",(dt,column,row,rain_mm))
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


# #Simulate reading one image
try:
    results = session.execute("select * from image where timestamp='%s' allow filtering"% (dt))
except:
    e = sys.exc_info()
    print("select error: ", e)

#Simulate reading based on x and y location
try:
    results = session.execute("Select * from image where X=1 and Y=1 allow filtering")
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
