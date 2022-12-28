import random

PRESENT = 1
WORKING_HOURS = 8
WAGE_PER_HOUR = 20

val = random.randint(0, 1)

if val == PRESENT:
    print("Employee is present.")
    print("Employee wage for day Rs.", WORKING_HOURS * WAGE_PER_HOUR)  # Use Case 2 Daily Employee Wage.

else:
    print("Employee is absent.")
