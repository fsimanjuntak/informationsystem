/*------------------------- Table customer ------------------------------*/
insert into customer(custno, cust_name, cust_addr, cust_phone) values ('C001','Frans Simanjuntak', 'Goudlaan 232 Groningen', 768499500);
update customer set cust_name = 'frans juanda simanjuntak' where custno = 'C001';
select * from customer;

/*------------------------- Table artist ------------------------------*/
insert into artist(artist_id, artist_name) values ('A001','jhon mayer');
insert into artist(artist_id, artist_name) values ('A002','taylor swift');
insert into artist(artist_id, artist_name) values ('A003','ed sheeran');
update artist set artist_name = 'jhon robert mayer' where artist_id = 'A001';
select * from artist;

/*------------------------- Table art ------------------------------*/
insert into art(art_code, art_title, artist_id) values ('ART001','Born and Raised','A001');
insert into art(art_code,art_title, artist_id) values ('ART002','Room For Squared','A001');
insert into art(art_code,art_title, artist_id) values ('ART003','Battle Studies','A001');
insert into art(art_code,art_title, artist_id) values ('ART004','Paradise Valley','A001');

insert into art(art_code,art_title, artist_id) values ('ART005','Red','A002');
insert into art(art_code,art_title, artist_id) values ('ART006','Speak Now','A002');
insert into art(art_code,art_title, artist_id) values ('ART007','Reputation','A002');

insert into art(art_code,art_title, artist_id) values ('ART008','You need Me','A003');
insert into art(art_code,art_title, artist_id) values ('ART009','The Orange Room','A003');
insert into art(art_code,art_title, artist_id) values ('ART010','X','A003');

select * from art;

/*------------------------- Table purchase ------------------------------*/
insert into purchase(custno,art_code,pur_date,price) values('C001','ART001', CURRENT_DATE, 100.00);
select * from purchase;
delete from purchase where custno='C001';
