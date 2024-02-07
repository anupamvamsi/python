def ChopList(inp_list):     # Modifies input list by removing first and last elements
    inp_list.pop(0)
    inp_list.pop(-1)

    return None


def MiddleJuice(inp_list):  # Returns middle elements of input list, in a separate list
    out_list = inp_list[1:-1]

    return out_list


file_handle = open("test.txt")
# count = 0

# for line_x in file_handle:
#     if count == 0:
#         # word = ((line_x.split())[1].split('@'))[1].split('.')
#         extracted_line = line_x.rstrip()
#     count += 1

# split_line = extracted_line.split()
# print(split_line)

# ChopList(split_line)
# print(split_line)

# middle_juiced_line = MiddleJuice(split_line)
# print(split_line)
# print(middle_juiced_line)

# split_line.append(["XXX"])                # '['XXX']' is added to split_line
# print(split_line)
# # split_line = split_line.append("YYY")     # 'None' will be stored in split_line
# split_line += ["ZZZ"]                     # 'ZZZ' will be added to split_line
# print(split_line)
# # split_line = split_line + "AAA"           # Error: Can't concat string to list


count = 0
for line_x in file_handle:
    words = line_x.split()
    # print('Debug:', words)
    if len(words) == 0:  # safeguards against empty lines
        continue
    if len(words) < 3:
        # safeguards against index out of range (only one or two words in a line)
        # since words[2] is being accessed, there at least have to be 3 words in 1 line
        continue
    if words[0] != 'From':
        continue
    count += 1
    print(count, words[2], end=" | ")

    ''' NO SUCH ERROR ANYMORE!
    # 1 Sat | Traceback (most recent call last):
    # File "c:\dev\vs_code\python\tut_files\0005_lists.py", line 50, in <module>
    # print(count, words[2], end=" | ")
    # IndexError: list index out of range
    '''
