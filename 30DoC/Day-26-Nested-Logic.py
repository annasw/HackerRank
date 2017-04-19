actualDay, actualMonth, actualYear = map(int, input().split())
dueDay, dueMonth, dueYear = map(int, input().split())

fine = 0
if actualYear > dueYear: # more than a year late
    fine = 10000
elif actualYear < dueYear:
    fine = 0
else: # year is the same
    if actualMonth > dueMonth: # at least one month late
        fine = 500*(actualMonth-dueMonth)
    elif actualMonth < dueMonth: # it's early
        fine = 0
    else: # same month
        if actualDay > dueDay: # at least a day late
            fine = (actualDay-dueDay)*15
        else: fine = 0

print(fine)
