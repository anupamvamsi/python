# CodeWars 0001
def reverse_words(text):
    # converting string input "text" to a list
    text = list(text)

    # To keep count of the letters to reverse each word individually
    count = 0

    # To store the positions of the spaces (" ") to insert them back in later
    spacePositions = []
    # To store the individually reversed words as single letters without the spaces (" ")
    val = []

    # For loop to store the positions of the spaces (" ")
    for i in range(len(text)):

        if text[i] == " ":
            spacePositions.append(i)
    
    # For loop to individually reverse every word and store the letters in a list
    for i in range(len(text)):
        if text[i] == " ":
            count = 0
        
        else:
            count += 1
            if i+1 == len(text):
                for j in range(i, i-count, -1):
                    val.append(text[j])
                    
            elif text[i+1] == " ":
                for j in range(i, i-count, -1):
                    val.append(text[j])
    
    # Storing the final string by concatenating all the letters 
    finalString = ""

    # To concatenate and generate single words
    if spacePositions == []:
        for i in range(len(text)):
            finalString += val[i]
    
    # To concatenate and generate whole sentences, taking into consideration all the spaces
    else:
        # To insert the spaces in the sentence
        for i in range(len(spacePositions)):
            val.insert(spacePositions[i], " ")
        
        # To concatenate and generate the final sentence
        for i in range(len(text)):
            finalString += val[i]
    
    return finalString


print(reverse_words("Hellooo    what  ldkjlj"))