# class_fourteen_numbers.py
# Class 14: Number Types & Basic Operations

print("=== Class 14: Number Types & Operations ===")

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")

def main_menu():
    print("\n--- Number Operations Menu ---")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Multiply Numbers")
    print("4. Divide Numbers")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Power")
    print("8. Check Type of Number")
    print("9. Exit")
    return input("Enter your choice (1-9): ")

def main():
    while True:
        choice = main_menu()

        if choice in ['1','2','3','4','5','6','7']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero!")
        elif choice == '5':
            if num2 != 0:
                print(f"Result: {num1} // {num2} = {num1 // num2}")
            else:
                print("Error: Division by zero!")
        elif choice == '6':
            if num2 != 0:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            else:
                print("Error: Division by zero!")
        elif choice == '7':
            print(f"Result: {num1} ** {num2} = {num1 ** num2}")
        elif choice == '8':
            num = get_number("Enter a number to check its type: ")
            if float(num).is_integer():
                print(f"{num} is an integer.")
            else:
                print(f"{num} is a float.")
        elif choice == '9':
            print("Exiting Number Operations Explorer. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    print("=== End of Class 14 ===")
    print()
