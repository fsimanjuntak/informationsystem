/*SQL syntax for case 1*/
CREATE KEYSPACE rainfallcase1
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE rainfallcase1;

CREATE TABLE image (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

/*SQL syntax for case 2*/
CREATE KEYSPACE rainfallcase2
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE rainfallcase2;

CREATE TABLE image (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

/*SQL syntax for case 3*/
CREATE KEYSPACE rainfallcase3
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE rainfallcase3;

CREATE TABLE week1 (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE week2 (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE week3 (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE week4 (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE week5 (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

/*SQL syntax for case 4*/
CREATE KEYSPACE rainfallcase4
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE rainfallcase4;


CREATE TABLE january (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE february (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE march (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE april (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE may (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE june (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE july (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE august (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE september (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE october (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE november (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);

CREATE TABLE december (
    TimeStamp timestamp,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY(TimeStamp, X, Y) 
);
