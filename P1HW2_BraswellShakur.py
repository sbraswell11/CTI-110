# Shakur Braswell
# October 1, 2023
# P1HW2_BraswellShakur.py
# This program calculates and displays travel expenses

# Get user input for travel expenses
print("-----------Travel Expenses Calculator-----------")
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("Enter the estimated gas expense: "))
accommodation_expense = float(input("Enter the estimated accommodation expense: "))
food_expense = float(input("Enter the estimated food expense: "))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Display travel expenses
print("\n-----------Travel Expenses-----------")
print("Destination:", destination)
print("Budget: $", budget)

print("Gas Expense", ": $", gas_expense)
print("Accommodation Expense", ": $", accommodation_expense)
print("Food Expense", ": $", food_expense)

print("Remaining Balance: $", budget - total_expenses)