#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """ State class definition """

    __tablename__ = 'states'
    
    id = Column(
                Integer,
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
