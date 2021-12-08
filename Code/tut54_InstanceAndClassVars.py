# Instance and Class Variables
class Employee:
    noOfLeaves = 8   # This will be same for all the objects of this class (Cannot be overwritten by using Objects)
    pass


harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 350
rohan.role = "Coordinator"

# print(harry.noOfLeaves)
# print(rohan.noOfLeaves)
print(Employee.noOfLeaves)

Employee.noOfLeaves = 9   # We can change any variable inside class through this, but if we try to change with an object it will create a new instance
print(Employee.noOfLeaves)

print(rohan.__dict__)
rohan.noOfLeaves = 10   # It will create a new instance
print(rohan.__dict__)
