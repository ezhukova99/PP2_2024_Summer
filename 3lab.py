#Python functions
#Create a function named my_function.
def my_function():
    print("Hello from a function")
#Execute a function named my_function.
def my_function():
  print("Hello from a function")

my_function()
#Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
   print(fname)
#Let the function return the x parameter + 5.
def my_function(x):
   return x + 5
#If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
  print("The youngest child is " + kids[2])
#If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(kid):
  print("His last name is " + kid["lname"])
#Create a lambda function that takes one parameter (a) and returns it.
x = lambda a : a
#Create a class named MyClass:
class MyClass:
  x = 5
#Create an object of MyClass called p1:
class MyClass:
   x = 5
p1 = MyClass()
#Use the p1 object to print the value of x:
class MyClass:
   x = 5
p1 = MyClass()
print(p1.x)
#What is the correct syntax to assign a "init" function to a class?
class Person: 
   def _init_(self, name, age):
      self.name = name
      self.age = age
#What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class Student(Person):
#We have used the Student class to create an object named x.
#What is the correct syntax to execute the printname method of the object x?
 class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()




