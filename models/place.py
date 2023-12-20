#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import String, Column, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place",
                           cascade="all, delete")
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False, backref='place_amenities')

    amenity_ids = []

    @property
    def reviews(self):
        """Getter attribute for reviews in FileStorage"""
        from models import storage
        reviews_list = []
        for rev in storage.all(Review).values():
            if rev.place_id == self.id:
                reviews_list.append(rev)
        return reviews_list

    @property
    def amenities(self):
        """
            return the list of Amenity
        """
        from models import storage
        from models.amenity import Amenity
        amenity_list = []
        for amenity in list(storage.all(Amenity).values()):
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, value):
        """
            adding an Amenity.id to the attribute amenity_ids
        """
        from models.amenity import Amenity
        if type(value) is Amenity:
            self.amenity_ids.append(value.id)
