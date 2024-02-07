# Removing punctuation and counting words from file
import string

file_handle = open("romeo_punc.txt")
punct = string.punctuation

punct_ascii_vals = {}
for punct_mark in punct:
    punct_ascii_vals[punct_mark] = ord(punct_mark)

print(punct_ascii_vals)

word_counts = {}
for line_x in file_handle:
    line_x = line_x.rstrip().lower()

    # maketrans('', '', punct) creates:
    ''' 
    # The following is a ASCII mapping of the characters, "!()-[]{};:'"\, <>./?@#$%^&*_~", 
    # to "None" type.
    {33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None, 64: None, 91: None, 92: None, 93: None, 94: None, 95: None, 96: None, 123: None, 124: None, 125: None, 126: None}
    '''

    # Generates the above ASCII mapping table to remove punctuation
    translation_table = line_x.maketrans('', '', punct)
    line_x = line_x.translate(translation_table)
    print(line_x)  # removed punctuation
    words = line_x.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

# print(word_counts)
