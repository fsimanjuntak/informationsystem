#This code is simulating writing 10 million data points to and reading them from cassandra database
import datetime
from datetime import timedelta
import sys
import random
from cassandra.cluster import Cluster

#Create connection to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('rainfallcase3')

#Define variables
max_column = 550
max_row = 500
dt = datetime.datetime.strptime("2016-01-01T00:00:00.000", "%Y-%m-%dT%H:%M:%S.%f")
column = 1
row = 1
counter = 1
table_counter = 1
counter_insert_to_table = 1
maxrow_in_table = 2016000

#Set current datetime before execution
currdatetimebeforeexecution = datetime.datetime.now()

#Simulate writing 10 million data points
for i in range (0,10000000):
    rain_mm = random.randint(15,60)
    try:
       session.execute("""INSERT INTO week%s (timestamp,x,y,amount) VALUES (%s,%s,%s,%s)""",(table_counter,dt,column,row,rain_mm))
       column = column+1
       counter = counter+1
       counter_insert_to_table = counter_insert_to_table+1
       if (column > 53):
           column = 1
           row = row + 1
       if (row > 50):
           row = 1
       if (counter > 1000):
           counter = 1
           dt = dt + datetime.timedelta(minutes = 5)

       if (counter_insert_to_table > maxrow_in_table):
           table_counter = table_counter+1
           counter_insert_to_table = 1

    except:
       e = sys.exc_info()
       print("insert error ", e)


arr_results=[]
#Simulate reading one image
try:
    for i in range (0,5):
        results = session.execute("select * from week%s where timestamp='%s' allow filtering"% (i+1,dt))
        arr_results.append(results)
except:
    e = sys.exc_info()
    print("select error: ", e)

#Simulate reading based on x and y location
try:
    for i in range (0,5):
        results = session.execute("select * from week%s where X=1 and Y=1 allow filtering"% (i+1))
        arr_results.append(results)
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
