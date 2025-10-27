#classfour_datatype_checking
# This script demonstrates basic data type checking in Python.
#data types: int, float, str, list, tuple, dict
#type() function is used to check the data type of a variable.
# classfour_datatype_checking.py
# Class Four: Data Type Checking

# 1. Using type()
x = 10
y = "Python"
z = [1, 2, 3]
a = 10.5
b = (4, 5, 6)
c= {'key': 'value'}
d=True
e=[ 'apple', 'banana', 'cherry']
f=[1.1, 2.2, 3.3]
g=range(1,10,3)
h=['Razz', 25, True]
j=frozenset([1,2,3,4])
k=True
l=None

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'list'>
print(type(a))  # <class 'float'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'dict'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'list'>]
print(type(f))  # <class 'list'>
print(type(g))  # <class 'range'>
print(type(h))  # <class 'list'>
print(type(j))  # <class 'frozenset'>
print(type(k))  # <class 'bool'>
print(type(l))  # <class 'NoneType'>
print()

# 2. Using isinstance()
print(isinstance(x, int))   # True
print(isinstance(y, (list, str)))  # True (because y is str)
print(isinstance(z, tuple)) # False
print()

# 3. issubclass() example
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
print()

# 4. Type comparison
a = 10
b = 10.5
print(type(a) == type(b))  # False

# 5. Practical check
data = {"name": "Razz", "age": 25}
if isinstance(data, dict):
    print("It's a dictionary ✅")
    print("Name:", data["name"])
    print("Age:", data["age"])
    print()