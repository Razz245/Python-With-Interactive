 # Class 13: Sentence & String Case Handling
print("=== Class 13: Sentence & String Case Handling ===")
text = input("Enter a sentence or string to explore: ")

while True:
    print("\n--- String Case Menu ---")
    print("1. Convert to Uppercase")
    print("2. Convert to Lowercase")
    print("3. Convert to Title Case")
    print("4. Swap Case")
    print("5. Strip Whitespace")
    print("6. Count Characters")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        print("Uppercase:", text.upper())
    elif choice == "2":
        print("Lowercase:", text.lower())
    elif choice == "3":
        print("Title Case:", text.title())
    elif choice == "4":
        print("Swap Case:", text.swapcase())
    elif choice == "5":
        print("Stripped Text:", text.strip())
    elif choice == "6":
        print("Total Characters (including spaces):", len(text))
        print("Total Words:", len(text.split()))
    elif choice == "7":
        print("Exiting String Case Explorer. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
        
print("=== End of Class 13 ===")
print()