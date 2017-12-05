
/*create database assignment2*/
create database assignment2;

/*create table person*/
create table person (
    id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    gender VARCHAR(50),
    country VARCHAR(50),
    PRIMARY KEY(id) 
);

/*Table friends*/
create table friends (
    person_id INT,
    friend_id INT,
    PRIMARY KEY(person_id,friend_id) 
);




