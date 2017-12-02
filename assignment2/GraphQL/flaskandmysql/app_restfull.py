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

#restful method that return a person
@app.route('/person/<userid>', methods=['GET'])
def getperson(userid):
    personobj = db_session.query(PersonModel).filter(PersonModel.id == userid).first()
    return json.dumps(personobj, cls=new_alchemy_encoder(), check_circular=False)

#restful method that return list of persons
@app.route('/person/list', methods=['GET'])
def listofpersons():
    listpersons = db_session.query(PersonModel).all()
    return json.dumps(listpersons, cls=new_alchemy_encoder(), check_circular=False)

if __name__ == '__main__':
    app.run(debug=True)

