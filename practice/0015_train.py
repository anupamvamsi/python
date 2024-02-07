class Train:
    def __init__(self, trainNo, trainName, tktCost):
        self.trainNo = trainNo
        self.trainName = trainName
        self.tktCost = tktCost

    def getTktCostAfterDiscount(self, discount):
        tktCostDiscounted = self.tktCost - (self.tktCost * (discount / 100.0))

        return tktCostDiscounted


class Railway:
    def __init__(self, zone, trainList):
        self.zone = zone
        self.trainList = trainList
        
    def getTrainTktCostAfterDiscount(self, trainNo, discount):
        flag = 0

        for train in self.trainList:
            if train.trainNo == trainNo:
                if discount > 0.0:
                    train.tktCost = train.getTktCostAfterDiscount(discount)
                else:
                    train.tktCost = train.tktCost

                flag = 1
                return train
                break

        if flag == 0:
            return None


if __name__ == "__main__":
    noOfTrains = int(input())
    ListOfTrains = []

    for trainNum in range(noOfTrains):
        trainNo = int(input())
        trainName = str(input())
        tktCost = float(input())

        trainObj = Train(trainNo, trainName, tktCost)
        ListOfTrains.append(trainObj)

    railwayObj = Railway("South Zone", ListOfTrains)

    tNSearch = int(input())
    discApply = float(input())

    returnValue = railwayObj.getTrainTktCostAfterDiscount(tNSearch, discApply)

    if returnValue == None:
        print("No Train Exists")
    else:
        print(returnValue.trainNo)
        print(returnValue.trainName)
        print(returnValue.tktCost)

# Sample Inputs:
'''
3
001
Pappu
230
002
Dappu
320
003
Mappu
203
002
25
'''

# Sample Output:
'''
2
Dappu
240.0
'''