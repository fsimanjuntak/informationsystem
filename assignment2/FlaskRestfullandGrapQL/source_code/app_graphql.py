from flask import Flask, render_template
from flask_graphql import GraphQLView
from database import db_session
from schema import schema
from datetime import timedelta
from flask_cors import CORS
from flask_jwt import JWT
from flask_jwt import jwt_required
import os
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'frans', 'testingapi'),
    User(2, 'stefan', 'testingapi'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.debug = True
# auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)

def graphql_view():
    # print ("verify_password", auth.verify_password)
    view = GraphQLView.as_view('graphql', schema=schema, context={'session': db_session}, graphiql=bool(app.config.get("DEBUG", False)))
    view = jwt_required()(view)
    return view

app.add_url_rule(
    '/graphql',
    view_func=graphql_view()
)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity


@app.route('/')
# @auth.login_required
def index():
	return ("Go to /graphql")

if __name__ == "__main__":
	app.run()


