import re

regex = re.compile('[^a-zA-Z_ ]')

word = (input())
word = regex.sub('', word)

print(word)
print(regex)

# Working Camel_Case (Astrome):
'''
Question Name:
Convert sentence into camel case.

Problem Statement:
The input sentence having a mix of valid and invalid identifier characters is to be converted to camel case valid identifier.

Constraints:
Any character which is not [A-Za-z_] is considered as a separator for words.
The number of characters in the line is less than 1000

________________________________________________________________________________
Ex:
Input Format:
"If you can, convert this 

Output Format:
"ifYouCanConvertThis"	
________________________________________________________________________________
'''

import string

special_chars = list(string.ascii_lowercase)
special_chars += list(string.ascii_uppercase)
special_chars += '_'

# Initial list of "text"
text = list(input())
# Using "changedText" to modify the case and remove special characters
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
        # To add the letters and their indexes after special characters
        changeCase[i+1] = text[i+1]
        # Removing the special characters 
        changedText.remove(text[i])

if text[last_index_check] not in special_chars:
    changedText.remove(text[last_index_check])
# To calculate the correct index of substituting the changed letter(s)
correctIndex = 0
# To count the number of special characters to substitute at the correct index
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

print(finalText)
