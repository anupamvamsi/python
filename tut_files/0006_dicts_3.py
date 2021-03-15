input_file = input("Enter file name: ")

try:
    file_handle = open(input_file)
except:
    print("No such file exists:", input_file)


day_committed_count = {}
histogram = {}
domains = {}

for line_x in file_handle:
    words = line_x.rstrip().split()
    len_words = len(words)

    if len_words == 0 or len_words < 3:
        continue

    if words[0] == "From":
        # ex-2 day of commit count
        day_committed_count[words[2]] = day_committed_count.get(
            words[2], 0) + 1

        # ex-3 histogram
        histogram[words[1]] = histogram.get(words[1], 0) + 1

        # ex-4 domain names
        domain_name = (words[1].split('@'))[1]
        domains[domain_name] = domains.get(domain_name, 0) + 1

# ex-4 max and min in histogram
hist_max_v = max(histogram.values())
hist_min_v = min(histogram.values())
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
hist_max_k = max(histogram, key=histogram.get)
hist_min_k = min(histogram, key=histogram.get)

# If there are multiple same values of min and max
hist_max_val_keys_list = {key for key,
                          value in histogram.items() if value == hist_max_v}
hist_min_val_keys_list = {key for key,
                          value in histogram.items() if value == hist_min_v}


# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
histogram = dict(sorted(histogram.items(), key=lambda item: item[1]))
print(f'\nSorted Histogram: {histogram}')


# ex-2 result
print(f'Days committed: {day_committed_count}')
# ex-3 result
print(f'\nHistogram: {histogram}')

# ex-4 results
print("\nHistogram Maxs:")
for max_key in hist_max_val_keys_list:
    print(f'({max_key}, {hist_max_v})')

print("\nHistogram Mins:")
for min_key in hist_min_val_keys_list:
    print(f'({min_key}, {hist_min_v})')

# ex-5 results
print("\nDomains:")
print(domains)
