class Doctor:
    def __init__(self, doctorID, doctorName, specialization, consultationFee):
        self.doctorID = doctorID
        self.doctorName = doctorName
        self.specialization = specialization
        self.consultationFee = consultationFee


class Hospital:
    def __init__(self, doctorDB, doctorNameSearchFor):
        self.doctorDB = doctorDB
        self.doctorNameSearchFor = doctorNameSearchFor

    def searchByDoctorName(self):
        docNameToSearch = self.doctorNameSearchFor
        docMatchedList = []
        flag = 0
        
        for doctorID in self.doctorDB.keys():
            if self.doctorDB[doctorID].doctorName == docNameToSearch:
                docMatchedList.append(self.doctorDB[doctorID])
                flag = 1
        
        if flag == 0:
            return None
        else:
            return docMatchedList

    def calculateConsultationFeeBySpecialization(self, specialization):
        totalConsultationFee  = 0
        
        for doctorID in self.doctorDB.keys():
            if self.doctorDB[doctorID].specialization == specialization:
                totalConsultationFee += self.doctorDB[doctorID].consultationFee
        
        return totalConsultationFee


if __name__ == "__main__":
    numOfDoctors = int(input())
    doctorDict = {}

    for num in range(numOfDoctors):
        doctorID = int(input())
        doctorName = str(input())
        specialization = str(input())
        consultationFee = int(input())

        doctorObject = Doctor(doctorID, doctorName, specialization, consultationFee)
        doctorDict.update({doctorID: doctorObject})

    docNameToSearchFor = str(input())
    specializationToMatch = str(input())

    hospitalObject = Hospital(doctorDict, docNameToSearchFor)

    searchDoctor = hospitalObject.searchByDoctorName()
    calculateFee = hospitalObject.calculateConsultationFeeBySpecialization(specializationToMatch)

    if searchDoctor == None:
        print("No doctor found. :(")
    else:
        for doctor in searchDoctor:
            print("Doctor ID: ", doctor.doctorID)
            print("Doctor name: ", doctor.doctorName)

    print("Consultation fee: ", calculateFee)


# Sample Input 1:
'''
4
001
sumbar
heart
200
002
rabmus
bone
100
003
barsum
bone
150
004
sumbar
heart
250
sumbar
bone
'''

# Sample Output 1:
'''
Doctor ID:  1                                                                                                          
Doctor name:  sumbar                                                                                                   
Doctor ID:  4                                                                                                          
Doctor name:  sumbar                                                                                                   
Consultation fee:  250
'''

# Sample Input 2:
'''
4
001
sumbar
heart
200
002
rabmus
bone
100
003
barsum
bone
150
004
sumbar
heart
250
rumbaroo
bone
'''