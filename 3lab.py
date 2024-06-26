"""
Define a class which has at least two methods: getString: to get a string from console 
input printString: to print the string in upper case.
"""
class StringHandler:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

"""
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

"""
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
"""
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points 
"""
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

"""
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        self.display_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied: Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        self.display_balance()

    def display_balance(self):
        print(f"Current balance: {self.balance}")

"""Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
"""
def is_prime(n):
    if n <= 1:#Numbers less than or equal to 1 are not prime, so the function returns False.

        return False
    if n == 2: # 2 is the only even prime number
        return True
    if n % 2 == 0: # Other even numbers are not prime
        return False
    for i in range(3, int(n**0.5) + 1, 2):#This loop checks for factors of n from 3 up to the square root of n, incrementing by 2 to skip even numbers.
        if n % i == 0:
            return False
    return True #If no divisors are found, the function returns True, indicating that n is a prime number.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23] #list of numbers from which we want to filter the prime numbers.
prime_numbers = list(filter(lambda x: is_prime(x), numbers)) 
"""
The filter function applies the is_prime function to each element in the numbers list.
Lambda function takes an element x and returns True if x is prime (i.e., is_prime(x) returns True).
"""
"""A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
"""
def grams_to_ounces(grams):
    ounces = grams * 0.03527396195
    return ounces

"""Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""
def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

"""Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs):
"""
def solve(numheads, numlegs):
    for chickens in range(numheads + 1): #Loop to iterate over possible numbers of chickens, from 0 to numheads.
        rabbits = numheads - chickens #For each possible number of chickens, it calculates the corresponding number of rabbits.
        if 2 * chickens + 4 * rabbits == numlegs:#It checks if the total number of legs matches the given numlegs. 
            return chickens, rabbits #If it does, it returns the number of chickens and rabbits.
    return None, None #If no valid solution is found, it returns None, None.

"""You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
"""
def is_prime(n): #The function is_prime checks if a number n is prime.
    if n <= 1:
        return False # returns False if n is less than or equal to 1.
    if n == 2:
        return True # True if n is 2 (the only even prime number).
    if n % 2 == 0:
        return False #False if n is even and greater than 2.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True #It checks for divisors from 3 up to the square root of n, skipping even numbers. If any divisor is found, it returns False. Otherwise, it returns True.

def filter_prime(numbers):
    return list(filter(is_prime, numbers))#It uses the filter function, which applies is_prime to each element in the numbers list.
#The result is converted to a list and returned.

"""
Write a function that accepts string from user and print all permutations of that string.
"""
from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))

"""
Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
"""
def reverse_sentence(sentence): #The function reverse_sentence takes a string sentence.
    words = sentence.split() #It splits the sentence into a list of words using the split method.
    reversed_words = words[::-1]#It reverses the list of words using slicing ([::-1]).
    return ' '.join(reversed_words)#It joins the reversed list of words into a single string with spaces in between and returns it.

"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
"""
def has_33(nums):#The function has_33 takes a list of numbers nums.
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:#It iterates over the list, checking each element and the next element.
            return True#If it finds two consecutive elements that are both 3, it returns True.
    return False#If no such pair is found, it returns False.

"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def spy_game(nums): #The function spy_game takes a list of numbers nums.
    code = [0, 0, 7]#It uses a list code to represent the sequence [0, 0, 7].
    for num in nums:#t iterates over the nums list. If the current number matches the first number in code, it removes that number from code
        if num == code[0]:
            code.pop(0)
        if not code:
            return True #If code becomes empty, it means the sequence [0, 0, 7] has been found in order, and the function returns True.
    return False #If the loop completes without finding the sequence, it returns False

"""
Write a function that computes the volume of a sphere given its radius
"""
import math

def volume_of_sphere(radius):
    return (4 / 3) * math.pi * radius**3

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
"""
def unique_elements(lst):#The function unique_elements takes a list lst.
    unique_lst = [] #It creates an empty list unique_lst.
    for elem in lst:#It iterates over each element in lst. If the element is not already in unique_lst, it adds the element to unique_lst.
        if elem not in unique_lst:
            unique_lst.append(elem)
    return unique_lst #It returns unique_lst, which contains only the unique elements from lst

"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""

def is_palindrome(string):#The function is_palindrome takes a string string.
    cleaned_string = ''.join(e for e in string if e.isalnum()).lower()#It removes all non-alphanumeric characters from the string and converts it to lowercase.
    return cleaned_string == cleaned_string[::-1]#It checks if the cleaned string is equal to its reverse using slicing (`[::-1]).
#It returns True if the cleaned string is a palindrome and False otherwise.

"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""
def histogram(lst):#The function histogram takes a list of integers lst.
    for num in lst:#It iterates over each number in the list.
        print('*' * num)#For each number, it prints a line of asterisks (*) of that length.

"""
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guess = None
    num_guesses = 0
    
    while guess != number_to_guess:#Initiates a loop that continues until the player guesses the correct number.
        guess = int(input("Take a guess.\n"))#Prompts the player to enter their guess and converts it to an integer.
        num_guesses += 1 #Increments the num_guesses variable to count the number of guesses made by the player.
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
    
    print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")

"""
Create a python file and import some of the functions from the above 13 tasks and try to use them.
"""
# main.py

from task1 import grams_to_ounces # type: ignore
from task2 import fahrenheit_to_centigrade # type: ignore # type: ignore
from task3 import solve # type: ignore
from task4 import filter_prime # type: ignore

def main():
    # Convert 100 grams to ounces
    print(grams_to_ounces(100))  # Output: 3.527396195
    
    # Convert 98 Fahrenheit to Centigrade
    print(fahrenheit_to_centigrade(98))  # Output: 36.666666666666664
    
    # Solve chickens and rabbits problem
    print(solve(35, 94))  # Output: (23, 12)
    
    # Filter prime numbers from a list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23]
    print(filter_prime(numbers))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23]

if __name__ == "__main__":
    main()


"""
This main.py file imports functions from different tasks and demonstrates their usage.
The main function calls each imported function with example inputs and prints the results.
This file serves as a way to test and showcase the functionalities implemented in the separate tasks.
"""

"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""
def is_above_5_5(movie):
    """
    Checks if a movie's IMDB score is above 5.5.
    
    Args:
    - movie (dict): Dictionary representing a movie with 'name', 'imdb', and 'category' keys.
    
    Returns:
    - bool: True if IMDB score is above 5.5, False otherwise.
    """
    return movie['imdb'] > 5.5

#Write a function that returns a sublist of movies with an IMDB score above 5.5.

def filter_by_imdb_above_5_5(movies):
    """
    Filters movies with an IMDB score above 5.5.
    
    Args:
    - movies (list): List of movie dictionaries.
    
    Returns:
    - list: List of movie dictionaries with IMDB score above 5.5.
    """
    return [movie for movie in movies if movie['imdb'] > 5.5]

#Write a function that takes a category name and returns just those movies under that category.
def filter_by_category(movies, category):
    """
    Filters movies by a specific category.
    
    Args:
    - movies (list): List of movie dictionaries.
    - category (str): Category name to filter movies.
    
    Returns:
    - list: List of movie dictionaries in the specified category.
    """
    return [movie for movie in movies if movie['category'] == category]


#Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb_score(movies):
    """
    Computes the average IMDB score of a list of movies.
    
    Args:
    - movies (list): List of movie dictionaries.
    
    Returns:
    - float: Average IMDB score of the movies.
    """
    if not movies:
        return 0.0
    
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

#Write a function that takes a category and computes the average IMDB score.
def average_imdb_score_by_category(movies, category):
    """
    Computes the average IMDB score of movies in a specific category.
    
    Args:
    - movies (list): List of movie dictionaries.
    - category (str): Category name to filter movies.
    
    Returns:
    - float: Average IMDB score of movies in the specified category.
    """
    category_movies = filter_by_category(movies, category)
    return average_imdb_score(category_movies)















