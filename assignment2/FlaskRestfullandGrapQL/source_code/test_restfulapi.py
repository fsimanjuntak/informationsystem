import requests
from requests.auth import HTTPDigestAuth
import json
import datetime
from datetime import timedelta

# Replace with the correct URL
baseurl = "http://127.0.0.1:5000/"
username = "frans"
password = "testingapi"

#url for each scenario
scenario_1 = "person/1?allfields=1&includingfriends=0"
scenario_2 = "person/1?allfields=0&includingfriends=0&desiredcolumns=first_name,country"
scenario_3 = "person/1?allfields=1&includingfriends=1"
scenario_4 = "person/1?allfields=1&includingfriends=1&friendsoffriend=1"

#new url
new_url = baseurl + scenario_1

#Set current datetime before execution
currdatetimebeforeexecution = datetime.datetime.now()

#call the api and store the response in a variable
response = requests.get(new_url,auth=(username, password), verify=True)

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
    print json_data
else:
  # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()
