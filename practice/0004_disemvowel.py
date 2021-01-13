# CodeWars 0002
def disemvowel(string):
    # Converting string input to two lists
    strin = list(string)
    string = list(string)

    # Making a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    # Detecting if vowels are in the string and removing them
    for i in range(len(string)):
        for j in range(len(vowels)):
            if string[i] == vowels[j]:
                strin.remove(string[i])
    
    # Rebuilding the string without any vowels
    stringfin = ""
    for i in range(len(strin)):
        stringfin += strin[i]
    return (stringfin)


print(disemvowel("Whattay wonderful world!"))