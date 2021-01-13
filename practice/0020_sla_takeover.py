def namesListBuilder():

    dictSchedule = {} # To count
    count = 1
    print("")
    print("---------------------------------------------------")
    print("START")
    print("---------------------------------------------------")
    inp = input(f"(Type 's' to stop)\nEnter name No. {count}: ")

    while inp.lower() != "s":
        dictSchedule[inp] = 0
        count += 1
        inp = input(f"Enter name No. {count}: ")
    
    print("---------------------------------------------------")

    return dictSchedule


def startTimeInput():

    strt = tuple(map(int, input("Enter the Start Time (in 24H, HH:MM format): ").split(":")))

    print("---------------------------------------------------")
    
    return strt


def getSchedule(namesList, startTime):

    dictNames = namesList
    namesList = list(namesList.keys())
    
    count = 0   # To keep cycling through the names every hour
    for time in range(startTime[0], 21):

        if time != 20 and startTime[1] > 0:

            if startTime[1] in range(1, 10):
                print(f'{namesList[count]} is supposed to ping SLA at: {time}:0{startTime[1]}')
            else:
                print(f'{namesList[count]} is supposed to ping SLA at: {time}:{startTime[1]}')
            dictNames[namesList[count]] += 1
            count += 1
            
        elif startTime[1] == 0:
            print(f'{namesList[count]} is supposed to ping SLA at: {time}:0{startTime[1]}')
            dictNames[namesList[count]] += 1
            count += 1
            
        if count >= len(namesList):
            count = 0

    print("---------------------------------------------------")
    
    for key in dictNames.keys():
        print(f'{key} pings SLA for a total of {dictNames[key]} time(s)!')
    
    print("---------------------------------------------------")


if __name__ == "__main__":
    names = namesListBuilder()
    start = startTimeInput()
    getSchedule(names, start)
    print("END")
    print("---------------------------------------------------")
    print("")


''' 
    # TESTS
    # def slaTakeover():
    #     namesList = list(map(str, input("Enter the names: ").split()))
    #     startTime = int(input("Enter start time in 24H format: "))

    #     count = 0
    #     for time in range(startTime, 21):
    #         print(namesList[count], time)
    #         count += 1
    #         if count >= len(namesList):
    #             count = 0


    # slaTakeover()

    # Sample input :
    # dee cee mee lee
    # a1 b2 c3 d4 e5 f6 g7 h8 i9

    # for time in range(startTime, 21):   # 21 because 9 PM, and we need to go till 8 PM
    #     # if time % startTime in range(len(namesList)):
    #         # print(namesList[time % startTime], time)
    #     # else:
    #     if len(namesList) <= startTime and time % startTime != 0:
    #         x = (time % startTime) % len(namesList)
    #     else:
    #         x = (time - startTime) % len(namesList)
    #     print(namesList[x], time)
'''