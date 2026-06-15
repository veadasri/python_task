# ============================================================
#   Expense Tracker — Task 2
#   Python Programming Internship
# ============================================================

import csv                      # built-in module to read/write CSV files
import os                       # to check if the file exists

FILE_NAME = "expenses.csv"      # all expenses will be saved in this file


# ── Function 1: Add an expense ───────────────────────────────
def add_expense():
    desc   = input("Enter expense description (e.g. Coffee): ")
    amount = input("Enter amount (e.g. 50): ")

    # Open file in "a" mode = append (adds to end, doesn't delete old data)
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])     # saves one row: Coffee, 50

    print("Expense added successfully!")


# ── Function 2: View all expenses ────────────────────────────
def view_expenses():
    # Check if the file exists at all
    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add one first!")
        return

    print("\n-------------------------------")
    print("  All Expenses")
    print("-------------------------------")

    # Open file in "r" mode = read
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:             # skip empty lines
                print(f"  Item: {row[0]},  Amount: ₹{row[1]}")

    print("-------------------------------")


# ── Function 3: View total spent ─────────────────────────────
def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add one first!")
        return

    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:             # skip empty lines
                total = total + float(row[1])   # row[1] is the amount

    print(f"\n  Total Amount Spent: ₹{total}")


# ── Function 4: Clear all expenses ───────────────────────────
def clear_expenses():
    confirm = input("Are you sure you want to clear all expenses? (yes/no): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w", newline="") as f:
            pass                # opening in "w" mode with nothing = empty file
        print("All expenses cleared!")
    else:
        print("Cancelled.")


# ── Menu ──────────────────────────────────────────────────────
def main():
    while True:
        print("\n========================================")
        print("       Expense Tracker — Task 2")
        print("========================================")
        print("  1. Add an expense")
        print("  2. View all expenses")
        print("  3. View total spent")
        print("  4. Clear all expenses")
        print("  0. Exit")
        print("----------------------------------------")

        choice = input("Choose an option (0-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            clear_expenses()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 0 to 4.")

main()