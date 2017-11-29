import json
from datetime import datetime

class MessageUtil(object):

    @staticmethod
    def constructMessage(input_datetime, input_x, input_y, input_amount):
       json_format = {'datetime':input_datetime, 'x':input_x, 'y':input_y, 'amount':input_amount}
       #for python 2.7 please remove the encod() method
       return (json.dumps(json_format))

    @staticmethod
    def extractMessage(obj):
        json_object = json.loads(obj)
        return json_object['id'], json_object['sender_type'], json_object['message_id'], json_object['message_type'], json_object['message'], json_object['messagedatetime']

    @staticmethod
    def convertStringToDateTime(str):
	    return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def convertDateTimeToString(obj):
	    return obj.strftime("%Y-%m-%d %H:%M:%S")
