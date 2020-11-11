'''
    SimplePerson class is create to test inheritance with MITPerson class.
'''
import datetime
import math


class Person(object):
    def __init__(self, name):
        self.name = name
        self.date_of_birth = None
        self.last_name = self.name.split(' ')[-1]

    def set_date_of_birth(self, year,month,day):
        self.date_of_birth = datetime.date(year,month,day)

    def get_age(self):
        if self.date_of_birth is None:
            return None
        return round(((datetime.date.today() - self.date_of_birth).days / 365), 1)

    def __lt__(self, other):
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    def __str__(self):
        return 'Name : ' + str(self.name) + ' \nAge : ' + str(self.get_age())