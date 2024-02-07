# py4e: ex-2
print("py4e: ex-2")
inp_name = input("Enter your name, please: ")
print("Hello, ", inp_name)

# py4e: ex-3
print("py4e: ex-3")
print("How long have you worked this week?")
inp_hours = input("Enter hours: ")
inp_rate = input("Enter rate: ")

try:
    f_hours = float(inp_hours)  # error here -> goes to except
    f_rate = float(inp_rate)    # error here -> goes to except
except:
    print("Enter valid input. Aborting program...")
    quit()  # quits immediately

if f_hours > 40:  # overtime
    regular = f_rate * f_hours
    overtime_pay = (f_hours - 40) * (f_rate * 0.7)
    pay = regular + overtime_pay
else:
    pay = f_rate * f_hours

print("Total pay: ", round(pay, 2))
print("--------------------")

# py4e: ex-4
print("py4e: ex-4")
width = 17
height = 12.0

print("Outputting random, (meaningless?) numbers...")
print(width//2)  # 8
print(width/2.0)  # 8.5
print(height/3)  # 4.0
print(1 + 2 * 5)  # 11

# py4e: ex-5
print("py4e: ex-5")
print("Let me check your temperature!")
inp_celsius = input("Enter temperature in °C: ")

try:
    f_celsius = float(inp_celsius)
except:
    print("Enter valid temperature input! Aborting program...")
    quit()

f_fahrenheit = round((f_celsius * 9. / 5.) + 32., 2)
print("Temperature in °F: ", f_fahrenheit)

if f_fahrenheit > 98.6 and f_hours >= 40:
    print("Working too hard, are we?")
elif f_fahrenheit > 98.6 and f_hours < 40:
    print("Getting a fever from barely breaking a sweat, hm...")
