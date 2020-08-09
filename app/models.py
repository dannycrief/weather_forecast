from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
metadata = Base.metadata


class Forecast(Base):
    __tablename__ = 'forecast'
    _id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False, nullable=False)
    city = Column(String(80), unique=False, nullable=False)
    temperature = Column(String(10), unique=False, nullable=False)
