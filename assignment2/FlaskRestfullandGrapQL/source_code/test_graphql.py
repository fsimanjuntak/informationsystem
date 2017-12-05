# from graphene.test import Client
from schema import schema
from gql import gql, Client
import requests
import json
import datetime
from datetime import timedelta
import urllib


#graphql url
url ="http://127.0.0.1:5000/graphql"
username = "frans"
password = "testingapi1"

#query for each scenario
query_scenario1 = '''
{
  findPerson(id:"1"){
    firstName
    lastName
    gender
    country

  }
}
'''

query_scenario2 = '''
{
  findPerson(id:"1"){
    firstName
    country
  }
}
'''

query_scenario3 = '''
{
  findPerson(id:"1"){
    firstName
    lastName
    gender
    country
    friends {
      firstName
      lastName
      gender
      country
    }
  }
}
'''

query_scenario4 = '''
{
  findPerson(id:"1"){
    firstName
    lastName
    gender
    country
    friends {
      firstName
      lastName
      gender
      country
      friends {
          firstName
          lastName
          gender
          country
        }
    }
  }
}
'''

#Set current datetime before execution
currdatetimebeforeexecution = datetime.datetime.now()

generated_token = "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNTEyNDgyNzcyLCJuYmYiOjE1MTI0ODI3NzIsImV4cCI6MTUxMjQ4MzA3Mn0.sUgOHR7YwqN5cesCsHf5-BDtvT1A4zmll1dIdzifM3o"
headers = {'Authorization': generated_token}

response = requests.get(url,auth=(username, password),json = {'query': query_scenario1}, headers=headers)

#Set current datetime before execution
currdatetimeafterexecution = datetime.datetime.now()

#Calculate delta beween datetime before and after execution
time_difference = currdatetimeafterexecution - currdatetimebeforeexecution
time_difference_in_seconds = time_difference.total_seconds()
print("Total execution time (in seconds) ", time_difference_in_seconds)

# For successful API call, response code will be 200 (OK)
if(response.ok):
    json_data = json.loads(response.content)
    print("The response contains {0} properties".format(len(json_data)))
    print("\n")
    for key in json_data:
        print str(json_data[key])
else:
  # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()
