from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import create_engine

engine = create_engine(
    'postgres+psycopg2://postgres:postgres@localhost:5432/tkinterDB')

session = Session(bind=engine)

Base = declarative_base()


class Addresses(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(Integer)

    def __repr__(self):
        return "<addresses(first_name={}, last_name={}, address={}, city={}, state={}, zipcode={})>".format(self.first_name, self.last_name, self.address, self.city, self.state, self.zipcode)


Base.metadata.create_all(engine)
