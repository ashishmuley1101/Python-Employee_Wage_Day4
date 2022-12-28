import random

PRESENT = 1
PRESENT_PART_TIME = 2
WORKING_HOURS = 8
WAGE_PER_HOUR = 20

val = random.randint(0, 2)

if val == PRESENT:
    print("Employee is present.")
    print("Employee wage for day Rs.", WORKING_HOURS * WAGE_PER_HOUR)  # Use Case 2 Daily Employee Wage.

elif val == PRESENT_PART_TIME:
    print("Employee is present for part time.")
    print("Employee wage for part time Rs.", WAGE_PER_HOUR * (WORKING_HOURS/2) ) # Use Case 3 Daily Employee Wage.

else:
    print("Employee is absent.")
