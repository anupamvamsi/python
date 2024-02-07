count = 0
sum_num = 0
small = 0
big = 0

while(True):
    number = input("Enter a number: ")
    if number.lower() == "done":
        print(f"Total: {sum_num} | Count: {count}", end="")
        print(f" | Average: {sum_num / count}")
        print(f"Max: {big} | Min: {small}")
        break
    try:
        f_number = float(number)
        count += 1
        sum_num += f_number
    except:
        print("Invalid input.")

    if small is None or f_number <= small:
        small = f_number
    if big is None or f_number > big:
        big = f_number
