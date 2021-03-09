def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


repeat_lyrics()


def EnterName():
    inp_name = input("Enter your name, please: ")

    return inp_name


def ComputePay():
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

    return round(pay, 2)


def ConvertTemperature():
    inp_celsius = input("Enter temperature in °C: ")

    try:
        f_celsius = float(inp_celsius)
    except:
        print("Enter valid temperature input! Aborting program...")
        quit()

    f_fahrenheit = round((f_celsius * 9. / 5.) + 32., 2)

    return f_fahrenheit


name = EnterName()
pay = ComputePay()
temp = ConvertTemperature()

print("Hello, ", name)
print("Total pay: ", pay)
print("Temperature in °F: ", temp)

word = "bananana"
i = word.find("na")
print(i)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
