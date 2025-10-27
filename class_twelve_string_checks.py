"""
Class Twelve: String Properties & Checks
Check if string starts with a substring → startswith()

Check if string ends with a substring → endswith()

Find position/index of a substring → find() / rfind()

Check if string is alphanumeric → isalnum()

Check if string is alphabetic → isalpha()

Check if string is numeric/digits → isdigit()

Check if string is whitespace → isspace()

Check if string is titlecased → istitle()
"""

print("=== Class Twelve: String Properties & Checks ===")
text = input("Enter a string to explore: ")

while True:
    print("\n--- String Properties Menu ---")
    print("1. Starts with substring")
    print("2. Ends with substring")
    print("3. Find position of substring")
    print("4. Check if alphanumeric")
    print("5. Check if alphabetic")
    print("6. Check if digits only")
    print("7. Check if whitespace only")
    print("8. Check if titlecased")
    print("9. Exit")
    
    choice = input("Enter your choice (1-9): ")
    
    if choice == "1":
        sub = input("Enter substring to check start: ")
        #startswith() method
        print("Starts with substring?", text.startswith(sub))
        
    elif choice == "2":
        #endswitch() method
        sub = input("Enter substring to check end: ")
        print("Ends with substring?", text.endswith(sub))
        
    elif choice == "3":
        #substring find() method
        sub = input("Enter substring to find: ")
        idx = text.find(sub)
        if idx != -1:
            print(f"Substring found at index {idx}")
        else:
            print("Substring not found!")
            
    elif choice == "4":
        #isalnum() method
        print("Is alphanumeric?", text.isalnum())
        
    elif choice == "5":
        #isalpha() method
        print("Is alphabetic?", text.isalpha())
        
    elif choice == "6":
        #isdigit() method
        print("Is digits only?", text.isdigit())
        
    elif choice == "7":
        #isspace() method
        print("Is whitespace only?", text.isspace())
        
    elif choice == "8":
        #istitle() method
        print("Is titlecased?", text.istitle())
        
    elif choice == "9":
        # Exit
        print("Exiting String Checks Explorer. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please try again.")
print("=== End of Report ===")
print("Developed by Rajib Sharma")
print("28 October 2025")
print("=== End of Report ===")