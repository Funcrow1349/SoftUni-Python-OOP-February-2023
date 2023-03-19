#   You are provided with a code containing a class Prisoner and a class Person. A prisoner is obviously a person, but
#   since a prisoner is not free to move an arbitrary distance, the Person class can be named FreePerson, then the idea
#   that a Prisoner inherits FreePerson is wrong. Rewrite the code and apply the LSP (Liskov Substitution Principle).
#   Rework the following code:

import copy

class Person:

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False



prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
