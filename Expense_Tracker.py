import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount: ")) 
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    expense = {
        'amount': amount,
        'category': category.lower(),
        'date': date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return
    print("\n--- All Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. {exp['date']} - ₹{exp['amount']} ({exp['category']})")
    print()

def filter_by_category(expenses):
    cat = input("Enter category to filter: ").lower()
    filtered = [e for e in expenses if e['category'] == cat]
    if not filtered:
        print("No expenses in this category.\n")
        return
    print(f"\n--- Expenses in '{cat}' ---")
    for exp in filtered:
        print(f"{exp['date']} - ₹{exp['amount']}")
    print()

def get_summary(expenses):
    if not expenses:
        print("No expenses to summarize.\n")
        return
    total = sum(e['amount'] for e in expenses)
    categories = {}
    for e in expenses:
        cat = e['category']
        categories[cat] = categories.get(cat, 0) + e['amount']
    top_category = max(categories, key=categories.get)
    print("\n--- Summary ---")
    print(f"Total spent: ₹{total}")
    print(f"Top spending category: {top_category} (₹{categories[top_category]})\n")

def menu():
    expenses = load_expenses()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Select an option: ")
        print()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            filter_by_category(expenses)
        elif choice == '4':
            get_summary(expenses)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")

if __name__ == "__main__":
    menu()
