/*Applying caching on cassandra database*/

CREATE KEYSPACE rainfallcase4
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE testing4;

CREATE TABLE january (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE february (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE march (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE april (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE may (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE june (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE july (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE august (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE september (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE october (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE november (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };

CREATE TABLE december (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
)
WITH caching = { 'keys' : 'ALL', 'rows_per_partition' : '250' };


