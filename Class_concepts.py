#practice 01

class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
     def met(self):
      print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()




#Practice 02

class Person:
  def __init__(self, aname, aage):
    self.name = aname
    self.age = aage

p1 = Person("Saraj", 36)
print(p1.name)
#Output: Saraj





#Practice 03

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
        
        
        
        
#Practice 04

saraj = Employee("Saraj", 255, "Instructor")

# rohan = Employee()
# saraj.name = "Saraj"
# saraj.salary = 455
# saraj.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(saraj.salary)
print(saraj.role)
print(saraj.name)

