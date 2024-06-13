#The statement below would print a Boolean value, which one?
print(10>9)
#The statement below would print a Boolean value, which one?
print(10 == 9)
#The statement below would print a Boolean value, which one?
print(10<9)
#The statement below would print a Boolean value, which one?
print(bool("abc"))
#The statement below would print a Boolean value, which one?
print(bool(0))
#Multiply 10 with 5, and print the result.
print(10*5)
#Divide 10 by 2, and print the result.
print(10/2)
#Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits: 
    print("Yes, apple is a fruit!")
#Use the correct comparison operator to check if 5 is not equal to 10.
If:
5 != 10: # type: ignore
print("5 and 10 is not equal")
#Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")
#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)
#Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)
#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
#Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#Use a range of indexes to print the third, fourth, and fifth item in the tuple
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
#Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
#Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
#Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)
#Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)
#Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
#Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
#Print "Hello World" if a is greater than b.
a = 50
b = 10
if  a > b:
    print("Hello Wrold")
#Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
     print("Hello World")
a = 50
b = 10
if a == b:
     print("Yes")
else:
     print("No")
#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else: print("3")
#Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d: # type: ignore
    print("Hello")
#Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d: # type: ignore
  print("Hello")
#Complete the code block, print "YES" if 5 is larger than 2.
if 5 > 2:
    print("YES")
#Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
a = 2
b = 5
print("YES") if a == b else  print("NO")
#Use an if statement to print "YES" if either a or b is equal to c.
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")
#Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1
#Stop the loop if i is 3.
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
#In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else: 
   print("i is no longer less than 6")
#Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)
#In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
      continue
   print(x)
#Use the range function to loop through a code set 6 times.
for x in range(6):
   print(x)
#Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
       break
print(x)
#Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


