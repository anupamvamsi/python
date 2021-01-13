class Project:
    def __init__(self, projectID, projectName, manHours, technologyList, avgProjCost=0):
        self.projectID = projectID
        self.projectName = projectName
        self.manHours = manHours
        self.technologyList = technologyList
        self.avgProjCost = avgProjCost

    def calculateProjCost(self, rateManHour):
        projectCost = self.manHours * rateManHour
        
        return projectCost

class Organization:
    def __init__(self, orgName, projList):
        self.orgName = orgName
        self.projList = projList

    def projAvgCostByTechnology(self, projID, ratePerManHour):
        averageProjCostPrice = 0.0
        flag = 0
        
        for project in self.projList:
            if project.projectID == projID:
                averageProjCostPrice = project.calculateProjCost(ratePerManHour) / len(project.technologyList)
                project.avgProjCost = averageProjCostPrice
                flag += 1
                break
                
        if flag == 0:
            return None
        else:
            return project

if __name__ == "__main__":
    numberOfProjects = int(input())
    projectList = []

    for proj in range(numberOfProjects):
        projeID = int(input())
        projeName = str(input())
        totManHours = int(input())

        numOfTech = int(input())
        techList = []
        for tech in range(numOfTech):
            techList.append(str(input()))

        projectList.append(Project(projeID, projeName, totManHours, techList))
    
    org = Organization("Pharma", projectList)

    projIDToSearch = int(input())
    rateManHourRupees = int(input())

    returnValue = org.projAvgCostByTechnology(projIDToSearch, rateManHourRupees)

    if returnValue == None:
        print("No Project Exists")

    else:
        print("Output: ")
        print(projIDToSearch) 
        print(returnValue.projectName)
        print(returnValue.technologyList)
        print(returnValue.manHours)
        print(returnValue.avgProjCost)

# Sample Inputs:

'''
4
1
Banking
100
2
C
C++
2
Finance
200
3
C
C++
Java
3
Pharma
500
4
C
C++
Java
Python
4
Transport
150
1
Dot Net
3
200
'''

# Sample Output:
'''
3 Pharma ['C', 'C++', 'Java', 'Python') 500 25000.0
'''