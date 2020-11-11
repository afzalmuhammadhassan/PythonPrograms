from Animal import Animal


class Person(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age)
        self.set_name(name)

    def __str__(self):
        return 'Person : ' + str(self.get_name()) + ' : ' + str(self.get_age())

    def speak(self):
        print('hello')

    def age_diff(self,other):
        if self.get_age() > other.get_age():
            print(str(self.get_name()) + ' is elder then ' + str(other.get_name()))