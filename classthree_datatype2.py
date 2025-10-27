# Topic Six: Boolean, None, Set, and Mapping (Dictionary) Types
# Author: Razz
# Purpose: Practice different data types in Python

# ----------------------------
# Boolean Type
# ----------------------------
is_active = True
is_logged_in = False

print("=== Boolean Type ===")
print("is_active:", is_active)
print("is_logged_in:", is_logged_in)
print("Type of is_active:", type(is_active))
print("True as integer:", int(True))
print("False as integer:", int(False))
print("Comparison example (10 > 5):", 10 > 5)
print("Logical AND:", is_active and is_logged_in)
print("Logical OR:", is_active or is_logged_in)
print()

# ----------------------------
# None Type
# ----------------------------
nothing = None

print("=== None Type ===")
print("Value:", nothing)
print("Type:", type(nothing))

# Example use case
def check_status(status):
    if status is None:
        return "Status not provided"
    else:
        return "Status available"

print("Function output:", check_status(None))
print()

# ----------------------------
# Set Type
# ----------------------------
print("=== Set Type ===")
numbers = {1, 2, 3, 4, 4, 5}  # duplicate 4 ignored
print("Numbers Set:", numbers)
print("Type:", type(numbers))

numbers.add(6)
numbers.remove(3)
print("After Add/Remove:", numbers)

# Set operations
even = {2, 4, 6, 8}
odd = {1, 3, 5, 7}
print("Union:", even | odd)
print("Intersection:", even & numbers)
print("Difference:", numbers - even)
print()

# ----------------------------
# Mapping Type (Dictionary)
# ----------------------------
print("=== Mapping/Dictionary Type ===")
person = {
    "name": "Razz",
    "age": 25,
    "skills": ["Python", "Linux", "Git"],
    "active": True
}

print("Dictionary:", person)
print("Type:", type(person))
print("Access by key:", person["name"])
print("All keys:", person.keys())
print("All values:", person.values())

# Add new key-value pair
person["country"] = "Bangladesh"
print("After adding country:", person)

# Update & delete
person["age"] = 26
del person["active"]
print("After update & delete:", person)

# Dictionary iteration
for key, value in person.items():
    print(f"{key}: {value}")

print("\nAll data types practiced successfully ✅")
