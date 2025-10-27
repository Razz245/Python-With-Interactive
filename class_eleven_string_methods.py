
# class_eleven_string_methods.py
# Interactive Console Project
# Rajib Sharma - 27 October 2025

def main():
    print("=== Class Eleven: String Methods & Functions ===")
    user_string = input("Enter a string to explore: ")

    while True:
        print("\n--- String Methods Menu ---")
        print("1. Convert to Uppercase")
        print("2. Convert to Lowercase")
        print("3. Capitalize First Letter")
        print("4. Count Substring Occurrences")
        print("5. Check if String is Alphanumeric")
        print("6. Check if String is Alphabetic")
        print("7. Find Index of Substring")
        print("8. Replace Substring")
        print("9. Reverse String")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            print("Uppercase:", user_string.upper())

        elif choice == "2":
            print("Lowercase:", user_string.lower())

        elif choice == "3":
            print("Capitalized:", user_string.capitalize())

        elif choice == "4":
            sub = input("Enter substring to count: ")
            print(f"'{sub}' appears {user_string.count(sub)} times.")

        elif choice == "5":
            print("Is alphanumeric?", user_string.isalnum())

        elif choice == "6":
            print("Is alphabetic?", user_string.isalpha())

        elif choice == "7":
            sub = input("Enter substring to find index: ")
            index = user_string.find(sub)
            if index != -1:
                print(f"Substring found at index {index}")
            else:
                print("Substring not found!")

        elif choice == "8":
            old = input("Enter substring to replace: ")
            new = input("Enter replacement string: ")
            user_string = user_string.replace(old, new)
            print("Updated string:", user_string)

        elif choice == "9":
            print("Reversed string:", user_string[::-1])

        elif choice == "10":
            print("Exiting String Methods Explorer. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1-10.")

if __name__ == "__main__":
    main()
print("=== End of Report ===")
print("Developed by Rajib Sharma")
print("27 October 2025")
print("=== End of Report ===")