from unittest import TestCase

from Person import Person


class TestPerson(TestCase):
    def test_get_name(self):
        my_person = Person()
        self.assertEqual(my_person.get_name(), 'John Doe', "Default parameters do not work")

    def test_set_first(self):
        self.fail()

    def test_set_last(self):
        self.fail()
