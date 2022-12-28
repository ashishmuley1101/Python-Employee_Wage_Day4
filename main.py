import random

PRESENT = 1
PRESENT_PART_TIME = 2
WORKING_HOURS = 8
WAGE_PER_HOUR = 20
WORKING_MAX_HOURS = 100
WORKING_MAX_DAYS = 20
total_woking_hours_month = 0
total_woking_days_month = 0

# Use Case 6 Calculating Wage for Month(max 20 days) and Hours(max 100 hours).

while total_woking_hours_month <= WORKING_MAX_HOURS and total_woking_days_month < WORKING_MAX_DAYS:

    total_woking_days_month += 1

    val = random.randint(0, 2)

    if val == PRESENT:
        print("Day : ", total_woking_days_month)
        print("Employee is present.")
        # print("Employee wage for day Rs.", WORKING_HOURS * WAGE_PER_HOUR)
        total_woking_hours_month = total_woking_hours_month + WORKING_HOURS
        print("Total hours : ", total_woking_hours_month)

    elif val == PRESENT_PART_TIME:
        print("Day : ", total_woking_days_month)
        print("Employee is present for part time.")
        # print("Employee wage for part time Rs.", WAGE_PER_HOUR * (WORKING_HOURS/2))
        total_woking_hours_month = total_woking_hours_month + (WORKING_HOURS / 2)
        print("Total hours : ", total_woking_hours_month)

    else:
        print("Day :", total_woking_days_month)
        print("Employee is absent.")
        print("Total hours : ", total_woking_hours_month)

salary = total_woking_hours_month * WAGE_PER_HOUR
print("Employee total wage : $", salary, "USD")