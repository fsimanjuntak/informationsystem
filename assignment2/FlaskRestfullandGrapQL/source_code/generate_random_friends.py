#This code is simulating writing 100000 data points to and reading them from MySQL database
import datetime
from datetime import timedelta
import sys
import random
import MySQLdb

#Create connection to MySQL database
conn = MySQLdb.connect(host= "localhost",user="root",passwd="admin",db="assignment3")
session = conn.cursor()

all_persons_id = range(1, 11, 1)

for personid in range (0,10):
    total_random_friend = random.randint(1,10)
    # print(total_random_friend)

    friends_id_list = random.sample(all_persons_id, total_random_friend)
    # print(friends_id_list)

    for item in friends_id_list:
        friend_id = item
        if (personid != friend_id):
            try:
               session.execute("""INSERT into friends (person_id,friend_id) values(%s,%s)""",(personid,friend_id))
               conn.commit()
            except:
               e = sys.exc_info()
               print("insert error ", e)
