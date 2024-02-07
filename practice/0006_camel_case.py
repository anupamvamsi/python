# CodeWars 0003
# special_chars = list('0123456789`~!@#$%^&*() +-=[]\;\',./{|:"<}>?')
import string
special_chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
special_chars = list(string.ascii_lowercase)
special_chars += list(string.ascii_uppercase)
special_chars += '_'
print(special_chars)


def to_camel_case(text):
    # Initial list of "text"
    text = list(text)
    # Using "changedText" to modify the case and remove "-" and "_"
    changedText = list(text)

    # Storing the indexes and letters for which case has to be changed in
    # the dictionary "changeCase"
    changeCase = {}
    last_index_check = 0
    for i in range(len(text)):
        if text[i] not in special_chars:
            # To prevent index out-of-range error
            if i+1 == len(text):
                last_index_check = i
                break
            # To add the letters and their indexes after "-" or "_"
            changeCase[i+1] = text[i+1]
            # Removing the "-" and "_"
            changedText.remove(text[i])

    if text[last_index_check] not in special_chars:
        changedText.remove(text[last_index_check])
    # To calculate the correct index of substituting the changed letter(s)
    correctIndex = 0
    # To count the number of "-" and "_" to substitute at the correct index
    count = 0
    for key in changeCase:
        # If the letter is in lowercase
        if changeCase.get(key).islower():
            count += 1
            correctIndex = key - count
            changedText[correctIndex] = changeCase.get(key).upper()
        # If the letter happens to be in uppercase by default
        else:
            count += 1
            correctIndex = key - count
            changedText[correctIndex] = changeCase.get(key)

    # Rebuilding the "text" string
    finalText = ""
    for i in range(len(changedText)):
        if i == 0 and changedText[i].isupper():
            finalText += changedText[i].lower()
        else:
            finalText += changedText[i]

    return finalText

# text = list(input())
# changedText = list(text)

# changeCase = {}
# for i in range(len(text)):
#    if text[i] in special_chars:
#         if i+1 == len(text):
#             break
#         changeCase[i+1] = text[i+1]
#         changedText.remove(text[i])
# if text[i] not in special_chars:
#   changeCase[i] = text[i]
#   changedText.remove(text[i])

# correctIndex = 0
# count = 0
# for key in changeCase:
#     if changeCase.get(key).islower():
#         count += 1
#         correctIndex = key - count
#         changedText[correctIndex] = changeCase.get(key).upper()
#     else:
#         count += 1
#         correctIndex = key - count
#         changedText[correctIndex] = changeCase.get(key)


# finalText = ""
# for i in range(len(changedText)):
#     if i == 0 and changedText[i].isupper():
#         finalText += changedText[i].lower()
#     else:
#         finalText += changedText[i]
print(to_camel_case("what-Is-eet_bootiful?"))
# print(to_camel_case(""))
print(bool(""))
print(to_camel_case("If you can, convert this"))
