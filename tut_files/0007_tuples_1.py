input_file = input("Enter file name: ")

try:
    file_handle = open(input_file)
except:
    print("Error: Unable to open file. File does not exist:", input_file)


histogram = {}

for line_x in file_handle:
    words = line_x.rstrip().split()
    len_words = len(words)

    if len_words == 0 or len_words < 3:
        continue

    if words[0] == "From":
        email_id = words[1]
        histogram[email_id] = histogram.get(email_id, 0) + 1

print("\nHistogram:")
print(histogram)

# SORT BASED ON KEYS:
histogram_sorted_by_key = {}

# Returns list and stores it in var
list_histogram_sorted_by_key = sorted(histogram)
for k in sorted(histogram):
    histogram_sorted_by_key[k] = histogram[k]

print("\nHistogram sorted based on KEYS:")
print(histogram_sorted_by_key)

# SORT BASED ON VALUES:
histogram_sorted_by_val = {}
list_histogram_sorted_by_val = []

for k, v in histogram.items():
    list_histogram_sorted_by_val.append((v, k))

print("\nHistogram TUPLED LIST unsorted based on VALUES:")
print(list_histogram_sorted_by_val)

list_histogram_sorted_by_val = sorted(list_histogram_sorted_by_val)

print("\nHistogram TUPLED LIST sorted based on VALUES:")
print(list_histogram_sorted_by_val)

# Putting the sorted list back into a dictionary
for v, k in list_histogram_sorted_by_val:
    histogram_sorted_by_val[k] = v

print("\nHistogram sorted based on VALUES:")
print(histogram_sorted_by_val)
