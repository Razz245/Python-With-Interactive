# classfive_immutable_types.py
# Author: Rajib Sharma
# Topic: Immutable Data Types in Python

# Immutable types: int, float, bool, str, tuple, frozenset

print("=== Immutable Data Types Demo ===\n")

# Integer
a = 10
print(f"Integer before change: {a}")
b = a
a += 5
print(f"Integer after change: {a} (Old b: {b})")

# Float
x = 3.14
print(f"\nFloat before change: {x}")
y = x
x = 2.71
print(f"Float after change: {x} (Old y: {y})")

# String
s = "Python"
print(f"\nString before change: {s}")
t = s
s = s + "3.12"
print(f"String after change: {s} (Old t: {t})")

# Tuple
tup = (1, 2, 3)
print(f"\nTuple before change: {tup}")
try:
    tup[0] = 100
except TypeError as e:
    print("Tuple is immutable:", e)

# Frozenset
fs = frozenset({1, 2, 3})
print(f"\nFrozenset before change: {fs}")
try:
    fs.add(4)
except AttributeError as e:
    print("Frozenset is immutable:", e)

print("\nAll immutable types create new memory objects when changed.")
# Demonstrating memory addresses
