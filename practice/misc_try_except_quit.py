# credits: py4e

hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    hours_f = float(hours)  # error here -> goes to except
    rate_f = float(rate)    # error here -> goes to except
except:
    print("Invalid input!")
    quit()  # quits immediately

if hours_f > 40:  # overtime
    regular = rate_f * hours_f
    overtime_pay = (hours_f - 40) * (rate_f * 0.7)
    pay = regular + overtime_pay
else:
    pay = rate_f * hours_f

print("Total pay: ", pay)
