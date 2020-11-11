'''
    this class is created for testing inheritance from SimplePerson class.
'''
from SimplePerson import Person


class MITPerson(Person):
    next_Number = 1

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.next_Number
        MITPerson.next_Number += 1

    def __lt__(self, other):
        return self.idNum < other.idNum

    def __str__(self):
        return 'Name : ' + str(self.name) + '\n ID # ' + str(self.idNum)
