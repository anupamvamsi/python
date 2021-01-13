class Student:
    def __init__(self, studentID, studentName, studentEmail, studentAddress):
        self.studentID = studentID
        self.studentName = studentName
        self.studentEmail = studentEmail
        self.studentAddress = studentAddress


class StudentDirectory:
    def __init__(self, directoryID, studentList):
        self.directoryID = directoryID
        self.studentList = studentList

    def findPatternMatchFromStudentName(self, studentName):
        studentName = studentName.lower()
        studentNameList = list(studentName)
        matchedList = []

        for student in self.studentList:
            if studentNameList[0] == list(student.studentName.lower())[0]:
                if studentNameList[-1] == list(student.studentName.lower())[-1]:
                    matchedList.append(student.studentName)
        
        return matchedList
    
    def getEmailCount(self, domainName):
        domainName = domainName.lower()
        count = 0

        for student in self.studentList:
            if domainName in student.studentEmail.lower():
                count += 1

        return count


if __name__ == "__main__":
    numberOfStudents = int(input())
    studentList = []

    for number in range(numberOfStudents):
        studentID = int(input())
        studentName = str(input())
        studentEmail = str(input())
        studentAddress = str(input())

        studentObject = Student(studentID, studentName, studentEmail, studentAddress)
        studentList.append(studentObject)

    studentDirectoryObject = StudentDirectory(10, studentList)

    patternToSearch = str(input())
    domainNameToSearch = str(input())

    findingPatternMatch = studentDirectoryObject.findPatternMatchFromStudentName(patternToSearch)
    emailCount = studentDirectoryObject.getEmailCount(domainNameToSearch)

    if findingPatternMatch == []:
        print("No Student Found!")
    else:
        print(findingPatternMatch)

    if emailCount == 0:
        print("No such domain name found!")
    else:
        print(f'The {domainNameToSearch} mail address was found {emailCount} number of times!')


# Sample Input 1:
'''
6
001
Aprithlippy
msA@gaMail.com
Jumbi
002
Slippooli
mrB@yAMil.com
Lumay
003
Alibbitippy
msC@gAmaiL.cOm
Grenno
004
Aglippisy
mrD@GaMAiL.coM
Swaifaer
005
Dippriepe
msEee@GAMAIL.COM
Minngl
006
Wirripploo
msFFF@YAmIl.coM
Orglip
Alistariy
yamil.com
'''

# Sample Output 1:
'''
['Aprithlippy', 'Alibbitippy', 'Aglippisy']
The yamil.com mail address was found 2 number of times!
'''

# Sample Input 2:
'''
6
001
Aprithlippy
msA@gaMail.com
Jumbi
002
Slippooli
mrB@yAMil.com
Lumay
003
Alibbitippy
msC@gAmaiL.cOm
Grenno
004
Aglippisy
mrD@GaMAiL.coM
Swaifaer
005
Dippriepe
msEee@GAMAIL.COM
Minngl
006
Wirripploo
msFFF@YAmIl.coM
Orglip
Jrrligg
zsgamailg.com
'''

# Sample Output 2:
'''
No Student Found!
No such domain name found!
'''