file_name1 = "mbox-short.txt"
file_name2 = "mbox.txt"

file_handle1 = open(file_name1)
file_handle2 = open(file_name2)

hours_count = {}

for line_x in file_handle1:
    words = line_x.rstrip().split()
    len_words = len(words)

    if len_words == 0 or len_words < 6:
        continue

    if words[0] == "From":
        hour = int((words[5].split(':'))[0])
        hours_count[hour] = hours_count.get(hour, 0) + 1

print("\nUNSORTED Hours Count:")
print(hours_count)

sorted_hours_count = dict(sorted([(k, v) for k, v in hours_count.items()]))
print("\nSORTED Hours Count [DICT]:")
print(sorted_hours_count)

print("\nSORTED Hours Count [TUPLED LIST]:")
print(sorted([(k, v) for k, v in hours_count.items()]))
