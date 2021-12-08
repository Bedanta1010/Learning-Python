# Multiple Inheritance in Python
class Employee:
    noOfLeaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.noOfLeaves = newLeaves

    @classmethod
    def from_string(cls, string):
        return cls(*string.split('-'))


class Player:
    noOfGames = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printGame(self):
        return f"{self.game} is played by {self.name} !"


class CoolProgrammer(Employee, Player):   # The classes are order sensitive
    Languages = 'C++'

    def printLang(self):
        print(self.Languages)


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 255, "Student")

shubham = Player('Shubham', ["Football", "Cricket"])
# CoolProgrammer will initialize from Employee first
karan = CoolProgrammer('Karan', 4511, "Cool Programmer")
# If there is any var which in not present in CoolProgrammer then the var from first Constructor will be taken since Employee
# is defined before Player in CoolProgrammer Constructor
