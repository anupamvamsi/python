# CodeWars 0003
def to_camel_case(text):
    # your code here
    # Initial list of "text"
    text = list(text)
    # Using "changedText" to modify the case and remove "-" and "_"
    changedText = list(text)
    
    # Storing the indexes and letters for which case has to be changed in 
    # the dictionary "changeCase"
    changeCase = {}
    for i in range(len(text)):
        if text[i] == "_" or text[i] == "-":
            # To prevent index out-of-range error
            if i+1 == len(text):
                break
            # To add the letters and their indexes after "-" or "_"
            changeCase[i+1] = text[i+1]
            # Removing the "-" and "_"
            changedText.remove(text[i])
    
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
        finalText += changedText[i]
        
    return finalText

print(to_camel_case("what-Is-eet_bootiful?"))