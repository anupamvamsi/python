input_file = input("Enter file name: ")

try:
    file_handle = open(input_file)
except:
    print("File does not exist:", input_file)
    quit()

count = 0
for line_x in file_handle:
    words = line_x.rstrip().split()
    len_words = len(words)

    if len_words == 0 or len_words < 2:
        continue
    if words[0] == "From":
        print(words[1], end=" | ")
        count += 1

print(
    f"\n\nThere were {count} lines in the file with 'From' as the first word.")
