#Topic Five: Data Types and Variables

"""Data Types বলে দেয় একটি variable কী ধরনের মান (value) ধারণ করছে।
Python-এ সবকিছুই object, আর প্রতিটি object-এর একটি নির্দিষ্ট data type থাকে।"""


#Common Built-in Data Types in Python
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str
# 4. Set Types: set, frozenset
"""
Data Type	Example	Description
int	x = 10	Whole number (integer)
float	y = 10.5	Decimal number
str	name = "Rajib"	Text or string
bool	is_hacker = True	Boolean (True/False)
list	fruits = ["apple", "mango", "banana"]	Ordered, changeable, allows duplicates
tuple	colors = ("red", "green", "blue")	Ordered, unchangeable
set	nums = {1, 2, 3}	Unordered, no duplicates
dict	person = {"name": "Rajib", "age": 25}	Key-value pairs
"""

#Variable Naming Conventions and Best Practices

#Checking Data Type
x = 10
y = "Hello"
z = [1, 2, 3]
print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>
print(type(z))   # <class 'list'>

#Type Casting (Convert one type to another)
x = int(5.9)         # float → int
y = float(10)        # int → float
z = str(100)         # int → string
a = list((1, 2, 3))  # tuple → list

#Type Casting (Convert one type to another)
x = int(5.9)         # float → int
y = float(10)        # int → float
z = str(100)         # int → string
a = list((1, 2, 3))  # tuple → list

#Examples of Each Type

#string
name = "Python"
print(name.upper())  # PYTHON

#Integer & Float
a = 10
b = 3.5
print(a + b)  # 13.5

#Boolean
x = True
y = False
print(x and y)  # False

#List
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  # [10, 20, 30, 40]

#Tuple
coordinates = (10, 20)
print(coordinates[0])  # 10

#Set
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3}

#Dictionary
student = {"name": "Rajib", "age": 25, "subject": "Python"}
print(student["name"])  # Rajib

#Example:
# Mutable
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# Immutable
name = "Rajib"
name = name + " Sharma"
print(name)  # Rajib Sharma

#Mixed Example
person = {
    "name": "Rajib",
    "age": 25,
    "skills": ["Python", "Linux", "Cybersecurity"],
    "active": True
}

print(person["skills"][1])  # Linux
print(type(person))         # <class 'dict'>

#Range Dara Type Example
numbers = range(1, 10)
nunbers_list = list(numbers)
nunbers2=range(0,21,2)
print(nunbers_list)  # [1, 2, 3, 4
print(list(nunbers2)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(type(numbers))  # <class 'range'>
