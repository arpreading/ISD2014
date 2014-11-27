class Person:

    def __init__(self,name,year):
        self._name = name
        self._year = year
        
    
    def addName(self, name):
        self._name = name

    def addYear(self, year):
        self._year = year

    def __repr__(self):
        return (self._name + " was born in: " + str(self._year))

class Student(Person):
    def __init__(self, name, year,course):
        super().__init__(name, year)
        self._course = course

    def addCourse(self, course):
        self._course = course

    def __repr__(self):
        return (super().__repr__() + "\nand is studying " + self._course)

class Instructor(Person):
    def __init__(self, name, year, salary):
        super().__init__(name, year)
        self._salary = salary

    def addSalary(self, salary):
        self._salary = salary

    def __repr__(self):
        return (super().__repr__() + "\nand is paid £" + str(self._salary)+ " per annum")

    
