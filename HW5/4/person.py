import logging
import UserLoggers

class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        UserLoggers.person_logger.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            UserLoggers.person_logger.critical("Invalid age!")
        self._age = 0
