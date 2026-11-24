# Shakur Braswell
# October 24, 2026
# P2HW1_BraswellShakur.py
# Using dictio
print("-----------Travel Expenses Calculator-----------")
budget = float(input("Enter your budget: "))
destination = (input("Enter your travel destination: "))
gas_expense = float(input("Enter the estimated gas expense: "))
accommodation_expense = float(input("Enter the estimated accommodation expense: "))
food_expense = float(input("Enter the estimated food expense: "))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Display travel expenses
print("\n-----------Travel Expenses-----------")
print(f"{'destination:':<22}{destination}")
print(f"{'Budget:':<22}${budget:.2f}")

print(f"{'Gas Expense:':<22}${gas_expense:.2f}")
print(f"{'Accommodation:':<22}${accommodation_expense:.2f}")
print(f"{'Food Expense:':<22}${food_expense:.2f}")

print(f"{'Remaining Balance:':<22} ${budget - total_expenses:.2f}")