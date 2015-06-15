# -*- coding: utf-8 -*-


class People(list):
    """
    Person collection
    """

    def load(self, people_data):
        """
        Populate the people collection from a list
        """
        for person_data in people_data:
            person = Person(person_data)
            self.append(person)
        self.build()

    def build(self):
        """
        Build the graph relation between people
        """
        for person in self:
            friend_ids = person['friends']
            friends = People([f for f in self if f['id'] in friend_ids])
            person['friend_ids'] = friend_ids
            person['friends'] = friends

    def get(self, person_id):
        """
        Get a person by id
        """
        for person in self:
            if person['id'] == person_id:
                return person
        return None

    def friends_of(self, person_id):
        """
        Get people in relation with a person
        """
        person = self.get(person_id)
        people = person.friends_level(1)
        for person in self:
            if person['friends'].get(person_id):
                people.append(person)
        return people

    def suggestion(self, person_id):
        """
        Retrieve people with no direct relation with a person but with at
        least 2 common friends
        """
        person = self.get(person_id)
        suggestion = People()
        friends = self.friends_of(person_id)
        not_friends = self.exclude(friends).remove(person)

        for person in not_friends:
            common = person['friends'].intersection(friends)
            if len(common) >= 2:
                suggestion.append(person)

        return suggestion

    def remove(self, person):
        """
        Remove a person from the collection
        """
        for index, current in enumerate(self):
            if current['id'] == person['id']:
                del self[index]
        return self

    def intersection(self, people):
        """
        Retrieve people existing in both collection
        """
        intersection = People()
        for person in self:
            if people.get(person['id']):
                intersection.append(person)
        return intersection

    def exclude(self, people):
        """
        Retrieve a collection without item from the collection
        """
        result = People()
        for person in self:
            if not people.get(person['id']):
                result.append(person)
        return result

    def __iadd__(self, people):
        """
        + operator merge collection VS summing them
        """
        union = self.clone()
        for person in people:
            union.append(person)
        return union

    def append(self, person):
        """
        Ensure person in the collection are unique
        """
        if not self.get(person['id']):
            list.append(self, person)

    def clone(self):
        """
        Clone the collection
        """
        return People(self[:])


class Person(dict):
    """
    Person model
    """

    def fullname(self):
        """
        Get the person fullname
        """
        text = self['surname'] and '{firstName} {surname}' or '{firstName}'
        return self.format(text)

    def format(self, text):
        """
        Format a text with current object attributes
        """
        return text.format(**self)

    def friends_level(self, level):
        """
        Retrieve people with a given number set to reach them
        """

        friends = self['friends']
        current_level = 1
        while current_level < level:
            current_friends = People()
            for friend in friends:
                current_friends += friend['friends']
            friends = current_friends
            current_level += 1
        return friends
