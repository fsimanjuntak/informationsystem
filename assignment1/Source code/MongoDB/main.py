# MongoDB is a document based NonSQL database that stores data in JSON formated documents.
# A collection contains more documents. It can be seen as the equivalent of a table in a SQL database.
# A database is a physical container for a group of collections. It gets its own files on the fyle system.

import pprint
import pymongo
from pymongo import MongoClient
from datetime import timedelta
from calendar import monthrange
import datetime
import random
from random import randint


class Matrix():
    rows = None,
    cols = None,
    number_of_datapoints = None,
    #stores pairs (x, y)
    coordinates = []
    #data to be written to DB
    #arrays to store values extracted from the above
    x = []
    y = []
    #array that stores values for precipitations
    val = []
    #timepstamp, one value epr image
    timestamp = None

    def __init__(self, m, n, datapoints):
        self.rows = m
        self.cols = n
        self.number_of_datapoints = datapoints

    def generateDataPoints(self):
        #as long as the list of coordinates does not have 1000 pairs of coordinates
        while(len(self.coordinates) < self.number_of_datapoints):
            #generate a new pair of coordinates
            (x, y) = (randint(0, self.rows), randint(0, self.cols))
            #check if it is already in the list
            if (x,y) not in self.coordinates:
                #if not in the list add it
                self.coordinates.append((x,y))
                #then generate a random value for precipitations
                self.val.append(round(random.uniform(0.0, 5.1), 3))
            #if the total number of coordinates was generated, exit while loop
            elif self.number_of_datapoints == len(self.coordinates):
                break
            #if the toal number of points was not generated or the generated pair is already in the list, continue with generating a new pair
            else:
                continue
        #once the coordinates and affernet values are generated, store coordinates eparately, so they can be easily addressed when wriiten to DB
        for tuple in self.coordinates:
            self.x.append(tuple[0])
            self.y.append(tuple[1])

def get_week_no(timestamp, initial_timestamp):
    day_number = (timestamp - initial_timestamp).days
    return int(day_number / 7)

def get_month_no(initial_timestamp, timestamp):
    delta = 0
    while True:
        mdays = monthrange(initial_timestamp.year, initial_timestamp.month)[1]
        initial_timestamp += timedelta(days=mdays)
        if initial_timestamp <= timestamp:
            delta += 1
        else:
            break
    return delta

def main():
    # 1. Connect to MongoDB instance running on localhost.
    # The result connection is used to access the databases from the MongoDB server
    mongodb_connection = MongoClient()

    # 2. If the database, with the specified name, does not exist, MongoDB will create it automatically.
    # Otherwise, it will be just accessed.
    database = mongodb_connection['Assignment1']

    #global data for number fo generated images
    number_of_images = (100, 1000, 10000, 100000)
    datapoints_per_image = 1000

    step = datetime.timedelta(seconds=300)

    for images_no in number_of_images:
        if images_no == 100:
            # global data used to generate timestamps
            timestamp = datetime.datetime(2017, 1, 1, 00, 00, 00)
            # total time for the writes
            wtotal = datetime.timedelta(0, 0)
            # total time for reading an image
            rimg_total = datetime.timedelta(0, 0)
            # total time for reading a datapoint
            rdatapoint_total = datetime.timedelta(0, 0)

            # 3. Get all existing collections. If any, delete all.
            existing_collections = database.collection_names()
            # if there are any collections in database, delete them
            if existing_collections:
                for collection_name in existing_collections:
                    temp = database[collection_name]
                    temp.drop()
            # 4. Create a collection for this case
            collection = database['Precipitations']

            # generate 100 matrices: one for each image holding precipitations data
            for i in range(0, images_no):
                # Documents are created as dictionaries, in python
                # Each document contains data for one image.
                new_matrix = Matrix(550, 500, datapoints_per_image)
                new_matrix.generateDataPoints()
                # for each new image, besides the 1st one, increase the timestamp by 5 minutes
                if i > 0:
                    timestamp += step
                new_matrix.timestamp = timestamp

                # store 1000 documents = all those afferent to an image
                docs_array = []

                for j in range(0, new_matrix.number_of_datapoints):
                    new_document = {"timestamp": new_matrix.timestamp,
                                    "x": new_matrix.x[j],
                                    "y": new_matrix.y[j],
                                    "value": new_matrix.val[j]
                                    }
                    docs_array.append(new_document)

                wbefore = datetime.datetime.now()
                # once all documents for an image were generated, bulk write them
                collection.insert_many(docs_array, True)
                wafter = datetime.datetime.now()
                wtotal += wafter - wbefore

            print wtotal

            rimg_before = datetime.datetime.now()
            print collection.find({"timestamp": datetime.datetime(2017, 1, 1, 8, 00, 00)}).count()
            rimg_after = datetime.datetime.now()
            rimg_total = rimg_after - rimg_before
            print rimg_total

            rdp_before = datetime.datetime.now()
            # count how many data points are retrieved
            print collection.find({"x": 315, "y": 348}).count()
            rdp_after = datetime.datetime.now()
            rdatapoint_total = rdp_after - rdp_before
            print rdatapoint_total

        if images_no == 1000:
            # global data used to generate timestamps
            timestamp = datetime.datetime(2017, 1, 1, 00, 00, 00)
            # total time for the writes
            wtotal = datetime.timedelta(0, 0)
            # total time for reading an image
            rimg_total = datetime.timedelta(0, 0)
            # total time for reading a datapoint
            rdatapoint_total = datetime.timedelta(0, 0)

            # 3. Get all existing collections. If any, delete all.
            existing_collections = database.collection_names()
            # if there are any collections in database, delete them
            if existing_collections:
                for collection_name in existing_collections:
                    temp = database[collection_name]
                    temp.drop()
            # 4. Create a collection for this case
            collection = database['Precipitations']

            # generate 1000 matrices: one for each image holding precipitations data
            for i in range(0, images_no):
                # Documents are created as dictionaries, in python
                # Each document contains data for one image.
                new_matrix = Matrix(550, 500, datapoints_per_image)
                new_matrix.generateDataPoints()
                # for each new image, besides the 1st one, increase the timestamp by 5 minutes
                if i > 0:
                    timestamp += step
                new_matrix.timestamp = timestamp

                # store 1000 documents = all those afferent to an image
                docs_array = []

                for j in range(0, new_matrix.number_of_datapoints):
                    new_document = {"timestamp": new_matrix.timestamp,
                                    "x": new_matrix.x[j],
                                    "y": new_matrix.y[j],
                                    "value": new_matrix.val[j]
                                    }
                    docs_array.append(new_document)

                wbefore = datetime.datetime.now()
                # once all documents for an image were generated, bulk write them
                collection.insert_many(docs_array, True)
                wafter = datetime.datetime.now()
                wtotal += wafter - wbefore

            print wtotal

            rimg_before = datetime.datetime.now()
            print collection.find({"timestamp": datetime.datetime(2017, 1, 1, 8, 00, 00)}).count()
            rimg_after = datetime.datetime.now()
            rimg_total = rimg_after - rimg_before
            print rimg_total

            rdp_before = datetime.datetime.now()
            # count how many data points are retrieved
            print collection.find({"x": 14, "y": 282}).count()
            rdp_after = datetime.datetime.now()
            rdatapoint_total = rdp_after - rdp_before
            print rdatapoint_total

        if images_no == 10000:
            # global data used to generate timestamps
            timestamp = datetime.datetime(2017, 1, 1, 00, 00, 00)
            initial_timestamp = timestamp
            # total time for the writes
            wtotal = datetime.timedelta(0, 0)
            # total time for reading an image
            rimg_total = datetime.timedelta(0, 0)
            # total time for reading a datapoint
            rdatapoint_total = datetime.timedelta(0, 0)

            # 3. Get all existing collections. If any, delete all.
            existing_collections = database.collection_names()
            # if there are any collections in database, delete them
            if existing_collections:
                for collection_name in existing_collections:
                    temp = database[collection_name]
                    temp.drop()

            # generate matrixes
            for i in range(0, images_no):
                # Documents are created as dictionaries, in python
                # Each document contains data for one image.
                new_matrix = Matrix(550, 500, datapoints_per_image)
                new_matrix.generateDataPoints()
                # for each new image, besides the 1st one, increase the timestamp by 5 minutes
                if i > 0:
                    timestamp += step
                new_matrix.timestamp = timestamp

                # get week number
                collection_index = get_week_no(timestamp, initial_timestamp)
                collection = database['Day ' + str(collection_index)]

                # store 1000 documents = all those afferent to an image
                docs_array = []

                for j in range(0, new_matrix.number_of_datapoints):
                    new_document = {"timestamp": new_matrix.timestamp,
                                    "x": new_matrix.x[j],
                                    "y": new_matrix.y[j],
                                    "value": new_matrix.val[j]
                                    }
                    docs_array.append(new_document)

                wbefore = datetime.datetime.now()
                # once all documents for an image were generated, bulk write them
                collection.insert_many(docs_array, True)
                wafter = datetime.datetime.now()
                wtotal += wafter - wbefore

            print wtotal

            rimg_before = datetime.datetime.now()
            tmstmp = datetime.datetime(2017, 1, 5, 8, 00, 00)
            # get the corresponding table for the given timestamp
            collection_index = get_week_no(tmstmp, initial_timestamp)
            collection = database['Day ' + str(collection_index)]
            print collection.find({"timestamp": tmstmp}).count()
            rimg_after = datetime.datetime.now()
            rimg_total = rimg_after - rimg_before
            print rimg_total

            existing_collections = database.collection_names()
            if existing_collections:
                for collection_name in existing_collections:
                    temp = database[collection_name]
                    rdp_before = datetime.datetime.now()
                    # count how many data points are retrieved
                    print temp.find({"x": 520, "y": 314}).count()
                    rdp_after = datetime.datetime.now()
                    rdatapoint_total += rdp_after - rdp_before
            print rdatapoint_total
        if images_no == 100000:
            # global data used to generate timestamps
            timestamp = datetime.datetime(2017, 1, 1, 00, 00, 00)
            initial_timestamp = timestamp
            # total time for the writes
            wtotal = datetime.timedelta(0, 0)
            # total time for reading an image
            rimg_total = datetime.timedelta(0, 0)
            # total time for reading a datapoint
            rdatapoint_total = datetime.timedelta(0, 0)

            # 3. Get all existing collections. If any, delete all.
            existing_collections = database.collection_names()
            # if there are any collections in database, delete them
            if existing_collections:
                for collection_name in existing_collections:
                    temp = database[collection_name]
                    temp.drop()

            # generate matrixes
            for i in range(0, images_no):
                # Documents are created as dictionaries, in python
                # Each document contains data for one image.
                new_matrix = Matrix(550, 500, datapoints_per_image)
                new_matrix.generateDataPoints()
                # for each new image, besides the 1st one, increase the timestamp by 5 minutes
                if i > 0:
                    timestamp += step
                new_matrix.timestamp = timestamp

                # get month number
                collection_index = get_month_no(initial_timestamp, timestamp)
                collection = database['Month ' + str(collection_index)]

                # store 1000 documents = all those afferent to an image
                docs_array = []

                for j in range(0, new_matrix.number_of_datapoints):
                    new_document = {"timestamp": new_matrix.timestamp,
                                    "x": new_matrix.x[j],
                                    "y": new_matrix.y[j],
                                    "value": new_matrix.val[j]
                                    }
                    docs_array.append(new_document)

                wbefore = datetime.datetime.now()
                # once all documents for an image were generated, bulk write them
                collection.insert_many(docs_array, True)
                wafter = datetime.datetime.now()
                wtotal += wafter - wbefore

            print wtotal

            rimg_before = datetime.datetime.now()
            tmstmp = datetime.datetime(2017, 7, 5, 8, 35, 00)
            # get the corresponding table for the given timestamp
            collection_index = get_month_no(tmstmp, initial_timestamp)
            collection = database['Month ' + str(collection_index)]
            print collection.find({"timestamp": tmstmp}).count()
            rimg_after = datetime.datetime.now()
            rimg_total = rimg_after - rimg_before
            print rimg_total

            existing_collections = database.collection_names()
            if existing_collections:
                for collection_name in existing_collections:
                    temp = database[collection_name]
                    rdp_before = datetime.datetime.now()
                    # count how many data points are retrieved
                    print temp.find({"x": 520, "y": 314}).count()
                    rdp_after = datetime.datetime.now()
                    rdatapoint_total += rdp_after - rdp_before
            print rdatapoint_total

if __name__ == "__main__":
    main()
