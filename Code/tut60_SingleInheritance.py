# Single Inheritance in Python
class Employee:
    noOfLeaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.noOfLeaves = newLeaves

    @classmethod
    def from_string(cls, string):
        return cls(*string.split('-'))


class Programmer(Employee):
    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages

    def printProg(self):
        return f"Programmer's name is {self.name}, role is {self.role} and salary is {self.salary}. The languages are {self.languages}"

    pass


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 255, "Student")

shubham = Programmer("Shubham", 570, "Programmer", ['Python'])
karan = Programmer("Karan", 815, "Programmer", ['Python', 'Java'])

print(karan.printProg())
print(shubham.printProg())
