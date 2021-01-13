# Version 1
def move_zeros1(array):
    # your code here
    arrayDem = array
        
    newArray = []
    count = 0
    for i in range(len(array)):
        if array[i] is 0 or array[i] is 0.0:
            count += 1
        elif array[i] is False:
            continue
    
    i = 0
    while count > 0:
        if array[i] is 0 or array[i] is 0.0:
            newArray.append(array[i])
            count -= 1
        elif array[i] is False:
            count -= 1
            continue
            
        i += 1
    
    countIndex = 0
    for i in range(len(arrayDem)):
        if arrayDem[i-countIndex] is 0 or arrayDem[i-countIndex] is 0.0:
            array.remove(arrayDem[i-countIndex])
            countIndex += 1
        elif array[i-countIndex] is False:
            continue
        
    for i in range(len(newArray)):
        arrayDem.append(newArray[i])
        
    return (arrayDem)


# Version 2
def move_zeros2(array):
    # your code here
    arrayDem = array
    
    newArray = []
    count = 0
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            count += 1
    
    i = 0
    while count > 0:
        if array[i] == 0 or array[i] == 0.0:
            newArray.append(array[i])
            count -= 1
        i += 1
    
    countIndex = 0
    for i in range(len(arrayDem)):
        if arrayDem[i-countIndex] == 0:
            array.remove(arrayDem[i-countIndex])
            countIndex += 1
        
    
    for i in range(len(newArray)):
        arrayDem.append(newArray[i])
        
    return (arrayDem)

