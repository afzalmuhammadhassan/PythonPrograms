from SimplePerson import Person
from MITPerson import MITPerson
p1 = Person('Muhammad Hassan Afzal')
p1.set_date_of_birth(1989, 12, 25)
p2 = Person('Omar Afzal')
p3 = Person('Muhammad Abdullah')

m1 = MITPerson('Hassan Afzal')
m2 = MITPerson('Muhammad Abdullah')
m3 = MITPerson('Omar Afzal')

m4 = Person('Hasan Yaseen')
m4.set_date_of_birth(2000,12,15)

mit = [m2, m1, m3,m4]
mit.sort()
for m in mit:
    print(m)
