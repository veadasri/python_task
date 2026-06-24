import csv
import os
from datetime import datetime      
FILE_NAME = "expenses.csv"

def add_expense():
    desc     = input("Enter expense description (e.g. Coffee): ")
    amount   = input("Enter amount (e.g. 50): ")
    category = input("Enter category (Food / Travel / Shopping / Other): ")

    date = datetime.now().strftime("%Y-%m")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, date])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add one first!")
        return

    print("\n--------------------------------------------------")
    print(f"  {'Description':<20} {'Amount':>8}  {'Category':<12}  {'Month'}")
    print("--------------------------------------------------")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                print(f"  {row[0]:<20} ₹{row[1]:>7}  {row[2]:<12}  {row[3]}")

    print("--------------------------------------------------")

def search_category():
    category = input("Enter category to search (e.g. Food): ")

    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add one first!")
        return

    print(f"\n--- Expenses in '{category}' ---")

    found = False
    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2].lower() == category.lower():  
                print(f"  {row[0]}  ₹{row[1]}  ({row[3]})")
                total = total + float(row[1])
                found = True

    if found:
        print(f"  Total spent on {category}: ₹{total}")
    else:
        print(f"  No expenses found for '{category}'.")

def total_per_category():
    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add one first!")
        return

    category_totals = {}      

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                cat    = row[2]
                amount = float(row[1])

                if cat in category_totals:
                    category_totals[cat] = category_totals[cat] + amount
                else:
                    category_totals[cat] = amount   # first time seeing this category

    print("\n--- Total Spent Per Category ---")
    for cat in category_totals:
        print(f"  {cat:<15}  ₹{category_totals[cat]}")

def monthly_total():
    month = input("Enter month (YYYY-MM, e.g. 2025-06): ")

    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add one first!")
        return

    total = 0
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[3] == month:    
                total = total + float(row[1])
                found = True

    if found:
        print(f"\n  Total spent in {month}: ₹{total}")
    else:
        print(f"  No expenses found for month: {month}")

def clear_expenses():
    confirm = input("Are you sure you want to clear all expenses? (yes/no): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w", newline="") as f:
            pass
        print("All expenses cleared!")
    else:
        print("Cancelled.")

def main():
    while True:
        print("\n========================================")
        print("     Expense Tracker 2.0 — Task 3")
        print("========================================")
        print("  1. Add an expense")
        print("  2. View all expenses")
        print("  3. Search by category")
        print("  4. Total spent per category")
        print("  5. Monthly total spending")
        print("  6. Clear all expenses")
        print("  0. Exit")
        print("----------------------------------------")

        choice = input("Choose an option (0-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_category()
        elif choice == "4":
            total_per_category()
        elif choice == "5":
            monthly_total()
        elif choice == "6":
            clear_expenses()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 0 to 6.")

main()