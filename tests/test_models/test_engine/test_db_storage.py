#!/usr/bin/python3
"""Module for testing database storage"""
import unittest
import sqlalchemy
from models import storage
from models.state import State
from models.city import City


class TestDBStorage(unittest.TestCase):
    """This Class tests the database storage methods"""
    def test_init(self):
        """"""
        self.assertIsNotNone(storage._DBStorage__engine)
        self.assertIsNotNone(storage._DBStorage__session)
        self.assertIsInstance(storage._DBStorage__engine,
                              sqlalchemy.engine.base.Engine)
        self.assertIsInstance(storage._DBStorage__session(),
                              sqlalchemy.orm.session.Session)

    def test_all(self):
        """Tests initializing"""
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.save()

        state_dict = self.storage.all(State)
        self.assertIn('State.{}'.format(state.id), state_dict)
        self.assertEqual(state_dict['State.{}'.format(state.id)], state)

        city_dict = self.storage.all(City)
        self.assertIn('City.{}'.format(city.id), city_dict)
        self.assertEqual(city_dict['City.{}'.format(city.id)], city)

        all_dict = self.storage.all()
        self.assertIn('State.{}'.format(state.id), all_dict)
        self.assertIn('City.{}'.format(city.id), all_dict)
        self.assertEqual(all_dict['State.{}'.format(state.id)], state)
        self.assertEqual(all_dict['City.{}'.format(city.id)], city)

    def test_new(self):
        """Tests adding new obj"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        queried_state = self.storage._DBStorage__session.query(
            State
            ).filter_by(name="California").first()
        self.assertIsNotNone(queried_state)
        self.assertEqual(queried_state.name, "California")

    def test_save(self):
        """Tests saving"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        queried_state = self.storage._DBStorage__session.query(
            State
            ).filter_by(name="California").first()
        self.assertIsNotNone(queried_state)
        self.assertEqual(queried_state.name, "California")
        queried_state.name = "New California"
        self.storage.save()
        updated_state = self.storage._DBStorage__session.query(
            State
            ).filter_by(name="New California").first()
        self.assertIsNotNone(updated_state)
        self.assertEqual(updated_state.name, "New California")

    def test_delete(self):
        """Tests deleting"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        queried_state = self.storage._DBStorage__session.query(
            State
            ).filter_by(name="California").first()
        self.assertIsNotNone(queried_state)
        self.assertEqual(queried_state.name, "California")
        self.storage.delete(queried_state)
        self.storage.save()
        deleted_state = self.storage._DBStorage__session.query(
            State
            ).filter_by(name="California").first()
        self.assertIsNone(deleted_state)

    def test_reload(self):
        """Tests reloading"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        state.name = "New California"
        self.storage.reload()
        reloaded_state = self.storage._DBStorage__session.query(
            State
            ).filter_by(name="New California").first()
        self.assertIsNone(reloaded_state)

    if __name__ == '__main__':
        unittest.main()
