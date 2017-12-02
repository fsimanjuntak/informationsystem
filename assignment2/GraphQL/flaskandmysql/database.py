from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, func, String
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm.collections import attribute_mapped_collection

engine = create_engine('mysql://root:admin@localhost:3306/assignment2', echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    gender = Column(String(255))
    country = Column(String(255))
    friends = relationship("Friends")

class Friends(Base):
    __tablename__ = "friends"
    friend_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))
