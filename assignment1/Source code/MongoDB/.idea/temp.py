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