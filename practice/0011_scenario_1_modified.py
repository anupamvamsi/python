# Scenario 1 (Modified)
def makeDictionaryOfPeopleBornInDifferentYears():
    numNames = int(input("Number of names: "))
    dictionary = {}

    for num in range(numNames):
        yearKey = int(input("Year: "))
        namesValues = str(input("Name: "))

        dictionary.setdefault(yearKey, [])
        dictionary[yearKey].append(namesValues)

    return dictionary


def findNumberOfPeopleBornInAYear(dictionary, year):
    if year in dictionary.keys():
        return len(dictionary.get(year))
    else:
        return None


dictionary = makeDictionaryOfPeopleBornInDifferentYears()
yearToSearch = int(input("What year do you want a count of? Enter: "))

numberOfPeopleBorn = findNumberOfPeopleBornInAYear(dictionary, yearToSearch)
print(dictionary)
print(f"Number of people born in the year {yearToSearch} is {numberOfPeopleBorn}.")