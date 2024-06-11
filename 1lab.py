#Code for output "Hello, World"
print("Hello, world!")
#Code for output "YES" if 5 is larger than 2
if 5>2:
 print("YES")
#We write comments in python with special character: #
#This is a comment
#To make multiline comment we use """
"""
This is a comment 
written in 
more than just one line
"""
#Code to cerate a variable named carname and assigned value Volvo to it
carname = "Volvo"
#To create variable named x and assigned value 50 to it:
x = 50
#To display sum 5+10, using two varibles x and y:
x = 5
y = 10
print(x+y)
#Create a variable called z, assign x + y to it, and display the result.
x = 5
y = 10
z = x + y
print(z)
#Insert the correct syntax to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
#Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = "Orange"
#Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
 global x
 x = "fantastic"

#The following code example would print the data type of x, what data type would that be?
x = 5
print(type(x))
#The following code example would print the data type of x, what data type would that be
x = "Hello, World"
print(type(x))
#The following code example would print the data type of x, what data type would that be?
x = 20.5
print(type(x))
#The following code example would print the data type of x, what data type would that be?
x = ["apple", "banana", "cherry"]
print(type(x))
#The following code example would print the data type of x, what data type would that be?
x = ("apple","banana", "cherry")
print(type(x))
#The following code example would print the data type of x, what data type would that be?
x = {"name": "John", "age": 36}
print(type(x))
#The following code example would print the data type of x, what data type would that be?
x = True
print(type(x))
#Insert the correct syntax to convert x into a floating point number.
x = 5
x = float(x)
#Insert the correct syntax to convert x into a integer.
x = 5.5
x = int(x)
#Insert the correct syntax to convert x into a complex number.
x = 5
x = complex(x)
#Use the len function to print the length of the string.
x = "Hello World"
print(len(x))
#Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
print(x)
#Get the characters from index 2 to index 4 (llo).
txt = "Hello, World"
x = txt[2:5]
print(x)
#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(x)
#Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
print(txt)
#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
print(txt)
#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)
#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))