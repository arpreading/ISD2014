class Person:

    def __init__(self):
        self._name = ""
        self._year = 0
    
    def addName(self, name):
        self._name = name

    def addYear(self, year):
        self._year = year

    def __repr__(self):
        return (self._name + " was born in: " + str(self._year))

class Student(Person):
    def __init__(self):
        super().__init__()
        self._course = ""

    def addCourse(self, course):
        self._course = course

    def __repr__(self):
        return (super().__repr__() + "  and is studying " + self._course)

class Instructor(Person):
    def __init__(self):
        super().__init__()
        self._salary = 0

    def addSalary(self, salary):
        self._salary = salary

    def __repr__(self):
        return (self._name + " is paid " + str(self._salary))    
