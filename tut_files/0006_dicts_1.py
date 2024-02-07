# Counting words from file
word = "good"

# method 1
dictionary = {}
for letter in word:
    if letter not in dictionary.keys():
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1

print(dictionary)

# method 2
dictionary = {}
for letter in word:
    dictionary[letter] = dictionary.get(letter, 0) + 1

print(dictionary)

# -----------------------------
file_handle = open("romeo.txt")

words = []
words_dict = {}
for line_x in file_handle:
    words += line_x.lower().split()
for word in words:
    words_dict[word] = words_dict.get(word, 0) + 1

print(words_dict)
print()
# for k, v in words_dict.items():
#     print(k, v, end=" | ")
