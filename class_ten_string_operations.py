
#!/usr/bin/env python3
# Class Ten: String Operations - Concatenation & Repetition
# Developed by Rajib Sharma
# Date: 27 October 2025

def string_concatenation():
    print("\n=== String Concatenation ===")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    
    full_name = first_name + " " + last_name
    print("Full Name:", full_name)

def string_repetition():
    print("\n=== String Repetition ===")
    word = input("Enter a word to repeat: ")
    
    while True:
        try:
            times = int(input("How many times to repeat? "))
            if times < 0:
                print("Please enter a positive number!")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")
    
    print("Repeated Output:", word * times)

def main():
    print("=== Welcome to Class Ten: String Operations ===")
    
    while True:
        print("\nMenu:")
        print("1. String Concatenation")
        print("2. String Repetition")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            string_concatenation()
        elif choice == "2":
            string_repetition()
        elif choice == "3":
            print("👋 Exiting. Keep practicing your strings!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
