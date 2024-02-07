class RescuedAnimal:
    def __init__(self, animalID, category, breed, healthStatus):
        self.animalID = animalID
        self.category = category
        self.breed = breed
        self.healthStatus = healthStatus


class AnimalAdoptionCentre:
    def __init__(self, centreID, rescuedAnimals):
        self.centreID = centreID
        self.rescuedAnimals = rescuedAnimals

    def countAnimalsPerCategory(self):
        dictionaryAnimals = {}
        
        for animal in self.rescuedAnimals:
            if animal.category not in dictionaryAnimals.keys():
                dictionaryAnimals.update({animal.category: None})
        
        for category in dictionaryAnimals.keys():
            count = 0
            for animal in self.rescuedAnimals:
                if category == animal.category:
                    count += 1
            dictionaryAnimals.update({category: count})
        #for category in dictionaryAnimals.keys():
        #    countCategory = 0

        #    for animal in self.rescuedAnimals:
        #        if category == animal.category:
        #            countCategory += 1
        #    dictionaryAnimals.update({animal.category: countCategory})

        return dictionaryAnimals

    def isAnimalForAdoption(self, animalID):
        flag = 0

        for animal in self.rescuedAnimals:
            if animal.animalID == animalID:
                if animal.healthStatus == "Healthy":
                    statusReturn = 1
                elif animal.healthStatus == "Unhealthy":
                    statusReturn = 2
                elif animal.healthStatus == "Traumatized":
                    statusReturn = 3
                elif animal.healthStatus == "Critical":
                    statusReturn = 4
                flag = 1
        
        if flag == 0:
            return 0
        else:
            return statusReturn


if __name__ == "__main__":
    numOfRescuedAnimals = int(input())
    rescuedAnimals = []

    for num in range(numOfRescuedAnimals):
        animalID = int(input())
        category = str(input())
        breed = str(input())
        healthStatus = str(input())

        rescuedAnimalObject = RescuedAnimal(animalID, category, breed, healthStatus)
        rescuedAnimals.append(rescuedAnimalObject)
    
    animalIDToSearch = int(input())

    adoptionCentreObject = AnimalAdoptionCentre(123, rescuedAnimals)

    countAnimalsPerCategoryOutput = adoptionCentreObject.countAnimalsPerCategory()
    isAnimalForAdoptionOutput = adoptionCentreObject.isAnimalForAdoption(animalIDToSearch)

    for key in countAnimalsPerCategoryOutput.keys():
        print(f'{key} {countAnimalsPerCategoryOutput[key]}')

    if isAnimalForAdoptionOutput == 0:
        print("Invalid Status Code")
    elif isAnimalForAdoptionOutput == 1:
        print(f'{animalIDToSearch} : Available for Adoption')
    elif isAnimalForAdoptionOutput == 2:
        print(f'{animalIDToSearch} : Undergoing Treatment')
    elif isAnimalForAdoptionOutput == 3:
        print(f'{animalIDToSearch} : Undergoing Trauma Care')
    elif isAnimalForAdoptionOutput == 4:
        print(f'{animalIDToSearch} : Unavailable for Adoption')

# Sample Input 1:
'''
4
23
Dog
Labrador
Healthy
12
Cat
British Shorthair
Unhealthy
45
Parrot
Macaw
Critical
68
Dog
PitBull
Traumatized
23
'''