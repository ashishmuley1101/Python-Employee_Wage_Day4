import random

PRESENT = 1
PRESENT_PART_TIME = 2
WORKING_HOURS = 8
WAGE_PER_HOUR = 20
WORKING_DAY_PER_MONTH = range(20)
total_woking_hours_month = 0




for day in WORKING_DAY_PER_MONTH:  # Use Case 5 Total wage for month (20 days).
    day += 1

    val = random.randint(0, 2)

    if val == PRESENT:
        print("Day : ", day)
        print("Employee is present.")
        # print("Employee wage for day Rs.", WORKING_HOURS * WAGE_PER_HOUR)
        total_woking_hours_month = total_woking_hours_month + WORKING_HOURS
        print("Total hours : ", total_woking_hours_month)

    elif val == PRESENT_PART_TIME:
        print("Day : ", day)
        print("Employee is present for part time.")
        # print("Employee wage for part time Rs.", WAGE_PER_HOUR * (WORKING_HOURS/2))
        total_woking_hours_month = total_woking_hours_month + (WORKING_HOURS / 2)
        print("Total hours : ", total_woking_hours_month)

    else:
        print("Day :", day)
        print("Employee is absent.")
        print("Total hours : ", total_woking_hours_month)

salary = total_woking_hours_month * WAGE_PER_HOUR  # Use Case 5 Total wage for month (20 days).
print("Employee total wage : $", salary, "USD")  # Use Case 5 Total wage for month (20 days).