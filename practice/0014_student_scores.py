class Student:
    def __init__(self, studentID, studentName, courseEnrolled, studentScore, studentGrade=''):
        self.studentID = studentID
        self.studentName = studentName
        self.courseEnrolled = courseEnrolled
        self.studentScore = studentScore
        self.studentGrade = studentGrade


class Department:
    def __init__(self, departmentName, studentList):
        self.departmentName = departmentName
        self.studentList = studentList

    def findCourseWiseStudents(self):
        courseWiseStudents = {}

        for student in self.studentList:
            if student.courseEnrolled not in courseWiseStudents.keys():
                courseWiseStudents.update({student.courseEnrolled: None})

        for course in courseWiseStudents.keys():
            studentCount = 0
            for student in self.studentList:
                if course == student.courseEnrolled:
                    studentCount += 1
            courseWiseStudents.update({course: studentCount})

        return courseWiseStudents

    def findStudentGrade(self, studentID):
        flag = 0

        for student in self.studentList:
            if student.studentID == studentID:
                if student.studentScore >= 80:
                    student.studentGrade = 'A'
                elif student.studentScore in range(65, 80):
                    student.studentGrade = 'B'
                elif student.studentScore in range(55, 65):
                    student.studentGrade = 'C'
                else:
                    student.studentGrade = 'F'
                flag = 1
                return student
                break
        
        if flag == 0:
            return None


if __name__ == '__main__':
    numberOfStudents = int(input())
    studentList = []

    for student in range(numberOfStudents):
        studentID = str(input())
        studentName = str(input())
        courseEnrolled = str(input())
        studentScore = int(input())

        studentObj = Student(studentID, studentName, courseEnrolled, studentScore)
        studentList.append(studentObj)

    departmentObj = Department("CS", studentList)

    gradeOfStudentID = str(input())

    returnCourseWiseStudents = departmentObj.findCourseWiseStudents()
    returnGrade = departmentObj.findStudentGrade(gradeOfStudentID)

    print(returnCourseWiseStudents)

    if returnGrade == None:
        print("No student with the specified student ID.")
    else:
        print("Student with ID: ", returnGrade.studentID)
        print(returnGrade.studentID)
        print(returnGrade.studentName)
        print(returnGrade.courseEnrolled)
        print(returnGrade.studentScore)
        print(returnGrade.studentGrade)

# Sample Inputs:
'''
10
ab
Mr A
Math
90
cd
Mr B
Math
70
ef
Mr C
Science
34
gh
Mr D
Math
62
ij
Mr E
PE
63
kl
Mr F
Math
23
mn
Mr G
PE
12
op
Mr H
Science
83
qr
Mr I
Science
61
st
Mr J
PE
92
qr
'''

# Sample Output:
'''
{'Math': 4, 'Science': 3, 'PE': 3}
C 
'''