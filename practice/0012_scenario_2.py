def createListOfFruits():
    fruityList = []
    fruit = str(input("Enter Fruitu!: "))

    while fruit != "stop".lower():
        fruityList.append(fruit)
        fruit = str(input("Enter one more fruitu!: "))
    print("Stoppedu!")

    return fruityList

def createFruityDictionary(fruityList):
    fruityDic = {}
    countFruit = 0

    for fruit in fruityList:
        if fruit not in fruityDic.keys():
            fruityDic[fruit] = 0

    for fruit in fruityDic.keys():
        countFruit = 0
        for fruity in fruityList:
            if fruit == fruity:
                countFruit += 1
        fruityDic.update({fruit: countFruit})
    
    return fruityDic

fruityListu = createListOfFruits()
fruityDictu = createFruityDictionary(fruityListu)

print("Outputtu: ", fruityDictu)