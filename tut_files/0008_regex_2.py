import re

file_handle = open('mbox-short.txt')
lst_numbers = []

for line_x in file_handle:
    line_x = line_x.rstrip()

    #  `findall` returns a list
    str_lst_num = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line_x)

    if len(str_lst_num) != 1:
        continue

    flt_num = float(str_lst_num[0])
    lst_numbers.append(flt_num)

print("Max: ", max(lst_numbers))
print("Min: ", min(lst_numbers))
