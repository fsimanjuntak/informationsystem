/*schema 100.000 data points*/
create database rainfallcase1;
use rainfallcase1;

CREATE TABLE image (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

/*schema 1 million data points*/
create database rainfallcase2;
use rainfallcase2;

CREATE TABLE image (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);


/*schema 10 million data points*/
create database rainfallcase3;
use rainfallcase3;

CREATE TABLE week1 (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE week2 (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE week3 (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE week4 (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE week5 (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);


/*schema 100 million data points*/
create database rainfallcase4;
use rainfallcase4;

CREATE TABLE january (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE february (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE march (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE april (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE may (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE june (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE july (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE august (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE september (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE october (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE november (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);

CREATE TABLE december (
    Timestamp datetime,
    X int,
    Y int,
    Amount float,
    PRIMARY KEY (Timestamp,X,Y)
);
