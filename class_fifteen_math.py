
#!/usr/bin/env python3
# Class 15: Math & Methods - Interactive Console Project
# Developed by Rajib Sharma
# 27 October 2025

import math
import random

def basic_operations():
    print("\n=== Basic Math Operations ===")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Error: Enter valid numbers!")
        return

    print(f"\nAddition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b if b != 0 else 'Error: Division by zero'}")
    print(f"Modulus: {a} % {b} = {a % b if b != 0 else 'Error: Division by zero'}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print(f"Floor Division: {a} // {b} = {a // b if b != 0 else 'Error: Division by zero'}")

def math_module_examples():
    print("\n=== Math Module Examples ===")
    try:
        num = float(input("Enter a number for math functions: "))
    except ValueError:
        print("Error: Enter a valid number!")
        return

    print(f"Square root: sqrt({num}) = {math.sqrt(num) if num >= 0 else 'Error: Negative number'}")
    print(f"Ceil: ceil({num}) = {math.ceil(num)}")
    print(f"Floor: floor({num}) = {math.floor(num)}")
    if num >= 0 and num.is_integer():
        print(f"Factorial: factorial({int(num)}) = {math.factorial(int(num))}")
    else:
        print("Factorial: Only non-negative integers allowed")
    print(f"Power: pow({num}, 2) = {math.pow(num, 2)}")
    print(f"Sine: sin({num}) = {math.sin(num)}")
    print(f"Cosine: cos({num}) = {math.cos(num)}")
    print(f"Tangent: tan({num}) = {math.tan(num)}")
    print(f"Radians: radians({num}) = {math.radians(num)}")
    print(f"Degrees: degrees({num}) = {math.degrees(num)}")

def random_module_examples():
    print("\n=== Random Module Examples ===")
    try:
        start = int(input("Enter start integer for random range: "))
        end = int(input("Enter end integer for random range: "))
    except ValueError:
        print("Error: Enter valid integers!")
        return

    print(f"Random integer between {start} and {end}: {random.randint(start, end)}")
    sample_list = ['Apple', 'Banana', 'Cherry', 'Date']
    print(f"Random choice from list {sample_list}: {random.choice(sample_list)}")
    shuffled = sample_list.copy()
    random.shuffle(shuffled)
    print(f"Shuffled list: {shuffled}")
    print(f"Random float between 0 and 1: {random.random()}")
    print(f"Random uniform float between {start} and {end}: {random.uniform(start, end)}")

def main():
    while True:
        print("\n=== Class 15: Math & Methods Menu ===")
        print("1. Basic Math Operations")
        print("2. Math Module Examples")
        print("3. Random Module Examples")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            basic_operations()
        elif choice == '2':
            math_module_examples()
        elif choice == '3':
            random_module_examples()
        elif choice == '4':
            print("Exiting Math & Methods Explorer. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
