# Shakur Braswell
# October 24, 2026
# P2HW2_BraswellShakur.py
#storing grades in a list



print("-----------Test Grades For Modules-----------")
Module_1 = float(input("Enter your grade for Module 1: "))
Module_2 = float(input("Enter your grade for Module 2: "))
Module_3 = float(input("Enter your grade for Module 3: "))
Module_4 = float(input("Enter your grade for Module 4: "))
Module_5 = float(input("Enter your grade for Module 5: "))
Module_6 = float(input("Enter your grade for Module 6: "))

grades = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

# Calculate the lowest grade, highest grade, sum of grades, and average of grades
lowest_grade = min(grades)
highest_grade = max(grades)
total = Module_1 + Module_2 + Module_3 + Module_4 + Module_5 + Module_6
average = total / len(grades)

# Display the results
print("\n-----------Test Results-----------")
print(f"{'Lowest Grade:':<22}{lowest_grade}")
print(f"{'Highest Grade:':<22}{highest_grade}")
print(f"{'Sum of Grades:':<22}{total}")
print(f"{'Average Grade:':<22}{average:.2f}")
