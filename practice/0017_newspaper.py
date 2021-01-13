class Newspaper:
    def __init__(self, regNo, publicationYear, newspaperName, price):
        self.regNo = regNo
        self.publicationYear = publicationYear
        self.newspaperName = newspaperName
        self.price = price

class NewspaperAgency:
    def __init__(self, newspaperDb):
        self.newspaperDb = newspaperDb

    def searchByYear(self, pubYear):
        matchedNewspaper = []
        count = 0

        for newspaper in self.newspaperDb.keys():
            if pubYear == self.newspaperDb[newspaper].publicationYear:
                matchedNewspaper.append(newspaper)
                count += 1

        if count == 0:
            return None
        else:
            return pubYear

    def calculatePriceByName(self, paperName):
        totalPrice = 0
        count = 0

        for newspaper in self.newspaperDb.keys():
            if paperName == self.newspaperDb[newspaper].newspaperName:
                totalPrice += self.newspaperDb[newspaper].price
                count += 1

        if count == 0:
            return count
        else:
            return totalPrice


if __name__ == "__main__":
    numberOfNewspapers = int(input())
    newspaperDictionary = {}

    for num in range(numberOfNewspapers):
        regNum = str(input())
        npYear = int(input())
        npName = str(input())
        npPrice = int(input())

        npObject = Newspaper(regNum, npYear, npName, npPrice)

        newspaperDictionary.update({regNum: npObject})

    npDict = NewspaperAgency(newspaperDictionary)

    pYear = int(input())
    nName = str(input())

    pubYearMatch = npDict.searchByYear(pYear)
    priceCalc = npDict.calculatePriceByName(nName)

    if pubYearMatch == None:
        print("No newspaper exists for the publication year")
    else:
        print(regNum)
        print(npYear)
        print(npName)
        print(npPrice)

    if priceCalc == 0:
        print("No newspapers with the given name")
    else:
        print("Total Price: ", priceCalc)

# Sample Inputs:
'''
3
RNI/101
1935
The Hindu
15
RNI/102
1967
Navbharat Times
7
RNI/103
1956
People Choice
15
1956
Navbharat Times
'''

# Sample Output for the Sample Inputs:
'''
RNI/103
1956
People Choice
15
Total Price:  7
'''