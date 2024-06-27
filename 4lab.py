"""
Q1:
Using data file sample-data.json, 
create output that resembles the following by parsing the included JSON file.
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
"""
import json

# Specify the path to sample-data.json
file_path = "/Users/eleonorazhukova/Downloads/sample-data.json"

# Load JSON data from file
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract relevant data from JSON
interfaces = data.get('imdata', [])

# Print table header
print("Interface Status")
print("=" * 80)
print("{:<60} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print each interface entry
for interface in interfaces:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<60} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))

#Q2: Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta 
# Current date and time
current_date = datetime.now()
print("Current date and time:", current_date)

# Subtract 5 days
new_date = current_date - timedelta(days=5)
print("Date and time five days ago:", new_date)

#Q3: Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

# Current date
today = datetime.now().date()
print("Today:", today)

# Yesterday
yesterday = today - timedelta(days=1)
print("Yesterday:", yesterday)

# Tomorrow
tomorrow = today + timedelta(days=1)
print("Tomorrow:", tomorrow)

#Q4: Write a Python program to drop microseconds from datetime.
from datetime import datetime 

# Current date and time with microseconds
current_datetime = datetime.now()
print("Current date and time with microseconds:", current_datetime)

# Drop microseconds
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Date and time without microseconds:", datetime_without_microseconds)

#Q5:Write a Python program to calculate two date difference in seconds.
from datetime import datetime

# Two sample dates
date1 = datetime(2023, 6, 1, 12, 0, 0)  # Year, Month, Day, Hour, Minute, Second
date2 = datetime(2023, 6, 10, 18, 30, 0) # Year, Month, Day, Hour, Minute, Second

# Calculate difference in seconds
difference = date2 - date1
difference_in_seconds = difference.total_seconds()
print("Difference in seconds:", difference_in_seconds)

#Q6: Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):#defines the generator function generate_squares which takes a single argument N
    for number in range(N): #The function uses  "for" loop to iterate from 0 to N-1
        yield number ** 2 # "yield" to generate the square of each number.

# Example usage:
N = 10  # Specify the upper limit
for square in generate_squares(N):
    print(square)

#Q7: Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def generate_even_numbers(n): #We define a function named generate_even_numbers that takes one argument n.
    for number in range(0, n + 1):#We use a for loop to iterate from 0 to n (inclusive).
        if number % 2 == 0: #nside the loop, we check if the number is even using the condition if number % 2 == 0.
            yield number #If the number is even, we yield it. This makes the function a generator.
n = int(input("Enter a number: ")) #Taking an integer input from the user.
10 #Example input
even_numbers = ', '.join(str(num) for num in generate_even_numbers(n))#generating the even numbers using the generator 
print(even_numbers) #printing them in a comma-separated format.

#Q8: Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for number in range(n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number
n = int(input("Enter a number: "))
divisible_numbers = list(divisible_by_3_and_4(n))
print("Numbers divisible by both 3 and 4 between 0 and", n, "are:", divisible_numbers)
50

#Q9: Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for num in range(a, b + 1):
        yield num * num

# Testing the generator with a for loop
a = 3
b = 7

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)

#Q10: Implement a generator that returns all numbers from (n) down to 0.

def countdown(n): #Defines the generator function countdown that takes one argument n.
    while n >= 0: #Starts a loop that continues as long as n is greater than or equal to 0.
        yield n #Yields the current value of n in each iteration.
        n -= 1 #Decrements n by 1 in each iteration to count down.

# Testing the generator with a for loop
n = 10

print(f"Counting down from {n} to 0:")
for number in countdown(n):
    print(number)

#Q11: Write a Python program to convert degree to radian.Input degree: 15. Output radian: 0.261904
import math

def degree_to_radian(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Example usage
degree_input = float(input("Input degree: ")) #Prompts the user to input the degree value and converts it to a float.
radian_output = degree_to_radian(degree_input) #Calls the degree_to_radian function with the input degree value to compute the corresponding radians.
print(f"Output radian: {radian_output}") #Prints the computed radian value.

15

"""
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""
def calculate_trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

# Example usage
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = calculate_trapezoid_area(height, base1, base2)
print(f"Expected Output: {area}")

5
5
6

"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
import math

def calculate_regular_polygon_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

# Example usage
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = calculate_regular_polygon_area(n, s)
print(f"The area of the polygon is: {area}")
4
25

"""
Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
"""

def calculate_parallelogram_area(base, height):
    area = base * height
    return area

# Example usage
base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = calculate_parallelogram_area(base_length, height)
print(f"Expected Output: {area}")

5
6
