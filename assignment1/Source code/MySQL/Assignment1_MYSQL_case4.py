#This code is simulating writing 100 million data points to and reading them from cassandra database
import datetime
from datetime import timedelta
import sys
import random
import MySQLdb

#Create connection to MySQL database
conn = MySQLdb.connect(host= "localhost",user="root",passwd="admin",db="rainfallcase4")
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

# Simulate writing 100 million data points
for i in range (0,100000000):
    rain_mm = random.randint(15,60)
    monthname = (dt.strftime('%B')).lower()

    try:
       CQLString = "INSERT INTO %s "%(monthname)
       CQLString = CQLString+"(timestamp,x,y,amount) VALUES (%s,%s,%s,%s)"
       session.execute(CQLString, (dt,column,row,rain_mm))
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

arr_results=[]
#Simulate reading one image
try:
    #Get month from parameter dt
    month_dt = (dt.strftime('%B')).lower()
    results = session.execute("select * from %s where timestamp='%s'"% (month_dt,dt))
    arr_results.append(results)
except:
    e = sys.exc_info()
    print("select error: ", e)

# #Simulate reading based on x and y location
arr_months = ['january','february','march','april','may','june','july','august','september','october','november','december']
try:
    for month in arr_months:
        results = session.execute("select * from %s where X=1 and Y=1"% (month))
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
