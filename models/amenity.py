#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
        class Amenity
        __tablename__: the name of table
        name: column
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
