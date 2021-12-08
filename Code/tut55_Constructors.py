# Self and __init__() (Constructors)
class Employee:
    noOfLeaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):  # here self will turn into object and we can access it
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 455, "Instructor") # This will always be handled by __init__(self)
print(f"Name is {harry.name}, salary is {harry.salary} and role is {harry.role}")

# harry = Employee()
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 350
# rohan.role = "Coordinator"
#
# print(rohan.printDetails())
# print(harry.printDetails())
