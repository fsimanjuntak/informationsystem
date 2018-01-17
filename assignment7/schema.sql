CREATE DATABASE assignment7
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;

CREATE TABLE customer (
    custno VARCHAR(20) NOT NULL PRIMARY KEY,
    cust_name VARCHAR(53) NOT NULL,
    cust_addr VARCHAR(50) NOT NULL,
    cust_phone INTEGER NOT NULL
);

CREATE TABLE artist (
    artist_id VARCHAR(20) NOT NULL PRIMARY KEY,
    artist_name VARCHAR(50) NOT NULL
);

CREATE TABLE art (
    art_code VARCHAR(20) PRIMARY KEY,
    art_title VARCHAR(50) NOT NULL,
    artist_id VARCHAR(20) NOT NULL REFERENCES artist(artist_id)
);

CREATE TABLE purchase (
    custno VARCHAR(20) NOT NULL REFERENCES customer(custno),
    art_code VARCHAR(20) NOT NULL REFERENCES art(art_code),
    pur_date DATE NOT NULL,
    price DECIMAL(7,2) NOT NULL,
    PRIMARY KEY (custno, art_title, pur_date)
);

/*2. ======================== Trigger ============================== */
/*1. Table customer*/
CREATE TRIGGER update_custname BEFORE INSERT OR UPDATE ON customer
    FOR EACH ROW EXECUTE PROCEDURE custnameToUppercase();

CREATE FUNCTION custnameToUppercase() RETURNS trigger AS $custnameToUppercase$
    BEGIN
        -- change custname to uppercase
        NEW.cust_name := UPPER(NEW.cust_name);
        RETURN NEW;
    END;
$custnameToUppercase$ LANGUAGE plpgsql;


/*2. Table artist*/
CREATE TRIGGER update_artistname BEFORE INSERT OR UPDATE ON artist
    FOR EACH ROW EXECUTE PROCEDURE artistnameToUppercase();

CREATE FUNCTION artistnameToUppercase() RETURNS trigger AS $artistnameToUppercase$
    BEGIN
        -- change custname to uppercase
        NEW.artist_name := UPPER(NEW.artist_name);
        RETURN NEW;
    END;
$artistnameToUppercase$ LANGUAGE plpgsql;


/*3. ======================== Trigger Transaction between 09.00 - 17.00 ============================== */
CREATE OR REPLACE FUNCTION checkNewTransaction() RETURNS trigger AS $checkNewTransaction$
    BEGIN
        IF(TO_CHAR(CURRENT_TIMESTAMP,'HH24:MM') NOT BETWEEN '09:00' AND '17:00') THEN 
		RAISE EXCEPTION 'Transaction is not allowed outside 09.00 and 17.00 office hours'; 
	END IF;
	RETURN NEW;
     END;
$checkNewTransaction$ LANGUAGE plpgsql;


CREATE TRIGGER check_transaction BEFORE DELETE OR INSERT OR UPDATE ON purchase
    -- Check transaction whether outside the 09:00h - 17:00h office hours
    FOR EACH ROW EXECUTE PROCEDURE checkNewTransaction();
