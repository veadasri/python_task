# ============================================================
#   Core Python Challenges — Task 1
#   Python Programming Internship
# ============================================================

# 1. Sum of Two Numbers
def sum_of_two():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    total = a + b
    print("Sum =", total)

# 2. Odd or Even Checker
def odd_or_even():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

# 3. Factorial Calculation
def factorial():
    n = int(input("Enter a number: "))
    result = 1
    for i in range(1, n + 1):   # loop from 1 to n
        result = result * i
    print("Factorial =", result)

# 4. Fibonacci Sequence
def fibonacci():
    n = int(input("How many terms? "))
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
    print()  # new line at the end

# 5. String Reverse
def string_reverse():
    s = input("Enter a string: ")
    reversed_s = s[::-1]        # slicing trick to reverse
    print("Reversed:", reversed_s)

# 6. Palindrome Check
def palindrome_check():
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    if word == reversed_word:
        print(word, "is a Palindrome")
    else:
        print(word, "is NOT a Palindrome")

# 7. Leap Year Check
def leap_year():
    year = int(input("Enter a year: "))
    if year % 400 == 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is NOT a Leap Year")
    elif year % 4 == 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is NOT a Leap Year")

# 8. Armstrong Number
def armstrong_number():
    n = int(input("Enter a number: "))
    digits = str(n)             # convert number to string to get digits
    power = len(digits)         # number of digits
    total = 0
    for d in digits:
        total = total + int(d) ** power
    if total == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is NOT an Armstrong number")


# ── Menu ──

def main():
    while True:
        print("\n========================================")
        print("   Core Python Challenges — Task 1")
        print("========================================")
        print("  1. Sum of Two Numbers")
        print("  2. Odd or Even Checker")
        print("  3. Factorial Calculation")
        print("  4. Fibonacci Sequence")
        print("  5. String Reverse")
        print("  6. Palindrome Check")
        print("  7. Leap Year Check")
        print("  8. Armstrong Number")
        print("  0. Exit")
        print("----------------------------------------")

        choice = input("Select a challenge (0-8): ")

        if choice == "1":
            sum_of_two()
        elif choice == "2":
            odd_or_even()
        elif choice == "3":
            factorial()
        elif choice == "4":
            fibonacci()
        elif choice == "5":
            string_reverse()
        elif choice == "6":
            palindrome_check()
        elif choice == "7":
            leap_year()
        elif choice == "8":
            armstrong_number()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 0 to 8.")

main()