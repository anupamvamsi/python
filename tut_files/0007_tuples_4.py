import string

punct = string.punctuation
punct += string.digits
punct += "‘’“”…—ôêéçàâè"
# https://stackoverflow.com/questions/6786609/how-to-remove-this-special-character
# \xef\xbb\xbf
punct += "\ufeff"   # This is the BOM - Byte Order Mark present at the beginning of a file
print(punct)
# punct += ' '
# print(punct)


# file_name = "mbox-short.txt"
# file_handle = open(file_name)

input_file = input("Enter file name: ")

try:
    file_handle = open(input_file, encoding='utf-8')
except:
    print("No such file exists:", input_file)


all_lines = ""
for line_x in file_handle:
    line_x = line_x.rstrip().lower()

    translation_table = line_x.maketrans('', '', punct)
    line_x = line_x.translate(translation_table)

    all_lines += line_x
    # print("".join(line_x.split()))

all_lines = "".join(all_lines.split())
# print(all_lines)


letter_dictionary = {}
for each_letter in all_lines:
    letter_dictionary[each_letter] = letter_dictionary.get(each_letter, 0) + 1

# Sorting based on key:
letter_dictionary_sorted_by_key = {}
list_letter_dictionary_sorted_by_key = sorted(letter_dictionary)

for letter_key in list_letter_dictionary_sorted_by_key:
    letter_dictionary_sorted_by_key[letter_key] = letter_dictionary[letter_key]

total_letters = 0

print("\nCOUNT OF EACH LETTER:")
for v in letter_dictionary_sorted_by_key.values():
    total_letters += v

# Final Table of results:
# Test files obtained from http://csweb.wooster.edu/nsommer/cs110/letter-frequency.html
# Check results with https://www.dcode.fr/frequency-analysis
for k, v in letter_dictionary_sorted_by_key.items():
    print(k, v, float(v / total_letters) * 100)

# some unknown character in alice.txt, holmes.txt, great_gatsby.txt
# It was the BOM - Byte Order Mark present at the beginning of a file
# 65279 in unicode
unk_char = (list(letter_dictionary_sorted_by_key.keys()))[-1]
print(unk_char, ord(unk_char))
