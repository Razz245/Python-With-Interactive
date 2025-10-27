# === Expense Tracker ===
print("=== Welcome to Your Expense Tracker ===")

# Dictionary to store expenses
expenses = {}

while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        category = input("Enter category (e.g., Food, Transport, Bills): ")
        amount = float(input("Enter amount (in Tk): "))

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        print(f"✅ {category} expense added successfully!")

    elif choice == '2':
        if not expenses:
            print("❌ No expenses recorded yet.")
        else:
            print("\n--- Expense List ---")
            for category, amount in expenses.items():
                print(f"{category}: {amount} Tk")

    elif choice == '3':
        total = sum(expenses.values())
        print(f"\n💰 Total Expense: {total} Tk")

    elif choice == '4':
        print("👋 Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Please enter between 1-4.")
# === End of Expense Tracker ===
print("=== Thank you for using the Expense Tracker ===")
print("Developed by Rajib Sharma")
print("27 October 2025")
print("=== End of Report ===")