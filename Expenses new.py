import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create file with headers if not exists
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

# Add expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")

# View expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) <= 1:
                print("No expenses found.\n")
                return

            print("\n--- Expense Records ---")
            for row in data:
                print("{:<12} {:<15} {:<10} {}".format(*row))
            print()

    except FileNotFoundError:
        print("Expense file not found.\n")

# Calculate total expenses
def total_expenses():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total += float(row["Amount"])

        print(f"\nTotal Expenses: ₹{total:.2f}\n")

    except FileNotFoundError:
        print("Expense file not found.\n")

# Main menu
def menu():
    initialize_file()

    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run program
menu()
