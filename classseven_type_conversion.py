# classseven_type_conversion.py
# Author: Rajib Sharma
# Topic: Type Conversion and Casting in Python

print("=== Type Conversion & Casting in Python ===\n")

# 1️⃣ Implicit Type Conversion (Automatic by Python)
x = 10
y = 2.5
result = x + y
print("Implicit Conversion Example:")
print(f"x = {x} (int), y = {y} (float) → result = {result} (type: {type(result)})\n")

# 2️⃣ Explicit Type Conversion (Manual Casting)
# Using int(), float(), str(), bool(), list(), tuple(), set(), dict()

print("Explicit Type Conversion Examples:")

# String → Integer
num_str = "100"
num_int = int(num_str)
print(f"String to Integer: {num_str} → {num_int}")

# Float → Integer
flt = 12.9
num_int2 = int(flt)
print(f"Float to Integer: {flt} → {num_int2}")

# Integer → Float
num = 5
num_float = float(num)
print(f"Integer to Float: {num} → {num_float}")

# Integer → String
num_str2 = str(num)
print(f"Integer to String: {num} → '{num_str2}'")

# String → Float
num_str3 = "45.6"
num_float2 = float(num_str3)
print(f"String to Float: '{num_str3}' → {num_float2}")

# Boolean Conversion
print("\nBoolean Conversion:")
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool('Hello') = {bool('Hello')}")

# List ↔ Tuple Conversion
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"\nList to Tuple: {my_list} → {my_tuple}")
print(f"Tuple to List: {my_tuple} → {list(my_tuple)}")

# Set Conversion
my_str = "hello"
my_set = set(my_str)
print(f"\nString to Set: '{my_str}' → {my_set}")

print("\n✅ All conversions completed successfully!")
