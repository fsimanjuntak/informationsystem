#create nested query and compare the complexity in how to implement this on restful and graphQL

#This code is simulating writing 100000 data points to and reading them from MySQL database
import datetime
from datetime import timedelta
import sys
import random
import MySQLdb
import json
from PersonModel import PersonModel
from FriendModel import FriendModel
from MessageUtil import MessageUtil
from flask import *

#function that returns the dictionary of the object
def obj_dict(obj):
    return obj.__dict__

#instantiate Flask framework
app = Flask(__name__)

#Create connection to MySQL database
conn = MySQLdb.connect(host= "localhost",user="root",passwd="admin",db="assignment2")
session = conn.cursor()

#restful method that return list of person
@app.route('/person/api/v1.0/getPerson', methods=['GET'])
def get_person():
    param_id = request.args.get('personid', default = 1, type = int)

    row_person = None
    res_person_friends = None
    try:

     #query person information
     session.execute("select * from person where id=%s"% (param_id))
     row_person = session.fetchone()

     #query friend list
     session.execute("select A.* from person A inner join friends B on A.id = B.friend_id where B.person_id=%s"% (param_id))
     res_person_friends = session.fetchall()

    except:
     e = sys.exc_info()
     print("select error: ", e)

    #Define variables
    person = None
    lst_person_friends = []

    #Loop person friends and add it on the list
    for row in res_person_friends:
        person_friend = FriendModel(row[0],row[1],row[2],row[3], row[4], row[5])
        lst_person_friends.append(person_friend)

    if (row_person != None):
        person = PersonModel(row_person[0],row_person[1],row_person[2],row_person[3], row_person[4], row_person[5], lst_person_friends)
        print("lst_person_friends ", len(lst_person_friends))
        # person.setFriendList(lst_person_friends)

    json_string = json.dumps(person, default=obj_dict)
    return jsonify({'person': json_string})

if __name__ == '__main__':
    app.run(debug=True)

