# classsix_mutable_types.py
# Author: Rajib Sharma
# Topic: Mutable Data Types in Python

print("=== Mutable Data Types Demo ===\n")

# List (Mutable)
numbers = [1, 2, 3]
print(f"Original list: {numbers}")
copy_numbers = numbers
numbers.append(4)
print(f"After append: {numbers} (copy_numbers also changed: {copy_numbers})")

# Dict (Mutable)
student = {"name": "Rajib", "age": 25}
print(f"\nOriginal dict: {student}")
copy_student = student
student["age"] = 26
print(f"After change: {student} (copy_student also changed: {copy_student})")

# Set (Mutable)
fruits = {"apple", "banana"}
print(f"\nOriginal set: {fruits}")
copy_fruits = fruits
fruits.add("cherry")
print(f"After add: {fruits} (copy_fruits also changed: {copy_fruits})")

# Checking memory identity (id)
print("\nChecking memory IDs:")
print(f"id(numbers): {id(numbers)}")
print(f"id(copy_numbers): {id(copy_numbers)}")

print("\n✅ Mutable objects keep the same memory reference when modified.")
