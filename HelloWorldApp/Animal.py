'''
simple test class for inharitance
'''
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return 'Animal : ' + str(self.name) + ' : ' + str(self.age)

    def set_name(self, new_name = ''):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Cat(Animal):
    def __init__(self, age):
        Animal.__init__(self, age)

    def __str__(self):
        return 'Cat : ' + str(self.name) + ' : ' + str(self.age)

    def speak(self):
        print('mew')


class Rabit(Animal):
    def __init__(self, age):
        Animal.__init__(self,age)

    def __str__(self):
        return 'Rabit :' + str(self.name) + ' : ' + str(self.age)

    def speak(self):
        print('meep')