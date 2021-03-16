file_handle = open('romeo.txt')

count_words = {}

for line_x in file_handle:
    words = line_x.rstrip().split()

    for word in words:
        count_words[word] = count_words.get(word, 0) + 1

print("\nUnsorted list:")
print(list(count_words))

print("\nSorted List WITH List Comprehension:")
print(sorted([(v, k) for k, v in count_words.items()]))

unsorted_list = []
for k, v in count_words.items():
    new_tuple = v, k
    unsorted_list.append(new_tuple)

sorted_list = sorted(unsorted_list)
print("\nSorted List WITHOUT List Comprehension:")
print(sorted_list)

print("\nDict Items:")
print(dict(list(count_words.items())))
