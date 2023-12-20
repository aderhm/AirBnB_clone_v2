#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import String, Column, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('user', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      Column('amenity_id', String(60),
                             ForeignKey('places.id')),
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
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="palce",
                           cascade="all, delete")
    amenities = relationship(
        'Amenity', secondary=place_amenity, viewonly=False, back_populates='place_amenities')

    @property
    def reviews(self):
        """Getter attribute for reviews in FileStorage"""
        from models import storage

        reviews_list = []
        for rev in storage.all(Review).values():
            if rev.place_id == self.id:
                reviews_list.append(rev)
        return reviews_list
