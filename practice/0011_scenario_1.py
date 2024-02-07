# Scenario 1
numNames = int(input("Number of names"))
dictionary = {}

for num in range(numNames):
    yearKey = int(input("Year: "))
    namesValues = str(input("Name: "))

    dictionary.setdefault(yearKey, [])
    dictionary[yearKey].append(namesValues)

print(dictionary)