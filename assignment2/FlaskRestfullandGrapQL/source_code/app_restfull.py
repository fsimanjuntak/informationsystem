import datetime
from datetime import timedelta
import sys
import random
import json
from flask import *
from sqlalchemy.orm import sessionmaker
from database import db_session, Person as PersonModel
import json
import os
from collections import namedtuple
from sqlalchemy.ext.serializer import loads, dumps
from sqlalchemy.ext.declarative import DeclarativeMeta
import numpy as np
from newpersonmodel import NewPersonModel
from flask_httpauth import HTTPBasicAuth

#function that returns the dictionary of the object
def obj_dict(obj):
    return obj.__dict__

def new_alchemy_encoder():
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder

#instantiate Flask framework
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if (username in ["frans","stefan"] and password=="testingapi"):
        return True


#restful method that return a person
@app.route('/person/<userid>', methods=['GET'])
@auth.login_required
def getperson(userid):
    allfields = (request.args.get('allfields', type = int))
    including_friends = (request.args.get('includingfriends',  type = int))
    desired_columns = request.args.get('desiredcolumns', type = str)
    friends_offriend = (request.args.get('friendsoffriend', type = int))

    if (allfields == 1):
        if (including_friends == 0):
            personobj = db_session.query(PersonModel).filter(PersonModel.id == userid).first()
            data = {'first_name': personobj.first_name, 'country': personobj.country, 'lastname':personobj.last_name, 'gender':personobj.gender }
            return json.dumps(data);
        else:
            personobj = db_session.query(PersonModel).filter(PersonModel.id == userid).first()

            lst_friends = []
            for fr in personobj.friends:
                friendobj = db_session.query(PersonModel).filter(PersonModel.id == fr.friend_id).first()

                arr_friends = []
                if (friends_offriend == 1):
                    for fr2 in friendobj.friends:
                        friendobj2 = db_session.query(PersonModel).filter(PersonModel.id == fr2.friend_id).first()
                        friend2 = NewPersonModel(friendobj2.id, friendobj2.first_name, friendobj2.last_name, friendobj2.gender, friendobj2.country,[])
                        arr_friends.append(friend2)

                friend = NewPersonModel(friendobj.id, friendobj.first_name, friendobj.last_name, friendobj.gender, friendobj.country,arr_friends)
                lst_friends.append(friend)

            newperson = NewPersonModel(personobj.id, personobj.first_name, personobj.last_name, personobj.gender, personobj.country, lst_friends)

            json_string = json.dumps(newperson, default=obj_dict)
            return jsonify({'person': json_string})

    else:
        arr_strcolumns = desired_columns.split(",")
        if "first_name" or "country" in arr_strcolumns:
            personobj = db_session.query(PersonModel).filter(PersonModel.id == userid).first()
            return json.dumps({'first_name': personobj.first_name, 'country': personobj.country });

#restful method that return list of persons
@app.route('/person/list', methods=['GET'])
@auth.login_required
def listofpersons():
    listpersons = db_session.query(PersonModel).all()
    return json.dumps(listpersons, cls=new_alchemy_encoder(), check_circular=False)

if __name__ == '__main__':
    app.run(debug=True)

