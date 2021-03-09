str = 'X-DSPAM-Confidence: 0.8475'
colon_pos = str.find(":")

f_num = float(str[colon_pos + 2:])
print(f_num)

# -----------------------------------
# Get the test file here: https://www.py4e.com/code3/mbox-short.txt
inp_file = input("Enter file name: ")
phrase = "X-DSPAM-Confidence:"
count = 0
total = 0

try:
    file_handle = open(inp_file)
except:
    if inp_file.lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File does not exist: ", inp_file)
    quit()

for line_x in file_handle:
    # print(line_x.rstrip())
    phrase_pos = line_x.find(phrase)

    if phrase_pos is not -1:
        f_num = float(line_x[phrase_pos + colon_pos + 2:])
        count += 1
        total += f_num
        # print(f_num, end=" ")

print(f"Average spam confidence: {total / count}")
