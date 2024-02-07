class Passenger():
    def __init__(self, passengerName, passengerAge):
        self.passengerName = passengerName
        self.passengerAge = passengerAge

    def passengers(self, age):
        if age >= 60:
            return "Senior citizen"
        elif age in range(18, 60):
            return "Normal"
        else:
            return "Below 18"

    def ageDictu(self, ageList):
        ageDic = {}

        for ageStatus in ageList:
            if ageStatus not in ageDic.keys():
                ageDic[ageStatus] = 0

        for ageStatus in ageDic.keys():
            countAgeStatus = 0
            for ageStatusInList in ageList:
                if ageStatus == ageStatusInList:
                    countAgeStatus += 1
            ageDic.update({ageStatus: countAgeStatus})

        return ageDic


if __name__ == "__main__":
    numOfPassengers = int(input("Number of Passengers: "))
    passengerList = []
    ageResult = []

    for num in range(numOfPassengers):
        pName = str(input("Name: "))
        pAge = int(input("Age: "))

        passengerObject = Passenger(pName, pAge)
        passengerList.append(passengerObject)

    for passenger in passengerList:
        ageResult.append(passenger.passengers(passenger.passengerAge))

    print("Passenger ages: ")
    for passenger in passengerList:
        print(passenger.passengerAge)

    print("Passenger status: ")
    print(ageResult)

    ageDictu = Passenger.ageDictu(passengerObject, ageResult)

    print("Age Dictionary: ")
    print(ageDictu)