# -*- encoding: utf-8 -*-

import os
import json
import pytest
from cargo.data import People


@pytest.fixture(scope="module")
def data():
    current_path = os.path.dirname(os.path.realpath(__file__))
    fixture_path = os.path.join(current_path, 'fixtures.json')
    data = None
    with open(fixture_path, 'r') as fixtures:
        data = json.load(fixtures)
    return data


class TestSocial():

    def test_load(self, data):
        """
        Check if the collection can be populated and data retrieved
        """
        people = People()
        people.load(data)

        assert len(people) == 20
        assert people[1]['firstName'] == 'Rob'

        person = people.get(2)
        assert person.fullname() == 'Rob Fitz'

    def test_direct_friends(self, data):
        """
        Retrieve direct friends from a person
        """
        people = People()
        people.load(data)

        friends = people.friends_of(2)

        assert len(friends) == 2
        assert friends[0].fullname() == 'Paul Crowe'
        assert friends[1].fullname() == 'Ben O\'Carolan'

    def test_two_steps_friends(self, data):
        """
        Retrieve 2 steps friends from a person
        """
        people = People()
        people.load(data)

        person = people.get(2)
        friends = person.friends_level(2)

        assert len(friends) == 4
        assert friends[0].fullname() == 'Rob Fitz'
        assert friends[1].fullname() == 'Victor'
        assert friends[2].fullname() == 'Peter Mac'
        assert friends[3].fullname() == 'Sarah Lane'

    def test_friend_suggestion(self, data):
        """
        Retrieve not direct friends who have at least 2 common friends with
        a person
        """
        people = People()
        people.load(data)

        suggestion = people.suggestion(5)

        assert len(suggestion) == 1
        assert suggestion[0].fullname() == 'Katy Couch'
