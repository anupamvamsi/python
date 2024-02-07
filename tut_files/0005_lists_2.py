input_file = input("Enter file name: ")
try:
    file_handle = open(input_file)
except:
    print("Unable to find file:", input_file)
    quit()

file_content = []
for line_x in file_handle:
    file_content += (line_x.rstrip().split())

print(file_content)

unique_words = []
for word in file_content:
    for next_word in file_content:
        if word is not next_word:
            if word not in unique_words:
                unique_words.append(word)

unique_words.sort()
print(unique_words)
