# Class Methods as Alternative Constructor
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
    def from_string(cls, string):   # Alternate constructor using class method
        # params = string.split('-')
        # return cls(params[0], params[1], params[2])
        return cls(*string.split('-'))


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 255, "Student")
karan = Employee.from_string("Karan-780-Coordinator")

print(karan.salary)

# print(harry.noOfLeaves)
# harry.changeLeaves(34)
# print(harry.noOfLeaves)
