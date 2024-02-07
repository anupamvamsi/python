class Customer:
    def __init__(self, orderID, customerName, address, customerType, orderAmount):
        self.orderID = orderID
        self.customerName = customerName
        self.address = address
        self.customerType = customerType
        self.orderAmount = orderAmount

class Store:
    def __init__(self, customerTypeIncentive, customerList):
        self.customerTypeIncentive = customerTypeIncentive  
        self.customerList = customerList

    def calculateBill(self, customerObject):
        if customerObject.customerType in self.customerTypeIncentive.keys():
            discount = customerObject.orderAmount * (self.customerTypeIncentive.get(customerObject.customerType) / 100.0)
            finalBill = customerObject.orderAmount - discount
            return finalBill
        else:
            return None

    def calculateCustomerBillByType(self, customerType):
        customerType.lower()
        dictionary = {}
        #finBill = 0.0
        flag = 0

        for customer in self.customerList:

            if customerType.lower() == customer.customerType.lower():
                finBill = self.calculateBill(customer)
                if finBill is not None:
                    dictionary.update({customer.orderID: finBill})
                    flag = 1

        if flag == 0:
            return None
        else:
            return dictionary


if __name__ == "__main__":

    numOfCustomerTypes = int(input())
    customerTypeIncentive = {}

    for num in range(numOfCustomerTypes):
        cType = str(input())
        incentivePercentage = float(input())

        customerTypeIncentive.update({cType: incentivePercentage})
    
    numOfCustomers = int(input())
    customerList = []

    for num in range(numOfCustomers):
        orderID = int(input())
        customerName = str(input())
        address = str(input())
        customerType = str(input())
        orderAmount = int(input())

        customerObject = Customer(orderID, customerName, address, customerType, orderAmount)
        customerList.append(customerObject)

    storeObject = Store(customerTypeIncentive, customerList)

    customerTypeInput = str(input())

    calculateBillValue = storeObject.calculateBill(customerList[0])
    
    if calculateBillValue == None:
        print("Customer Type Not Found.")
    else:
        print(calculateBillValue)

    calculateCustomerBillByTypeValue = storeObject.calculateCustomerBillByType(customerTypeInput)

    if calculateCustomerBillByTypeValue == None:
        print("Customer Not Found.")
    else:
        print(f"{list(calculateCustomerBillByTypeValue.keys())[0]} {calculateCustomerBillByTypeValue.get(list(calculateCustomerBillByTypeValue.keys())[0])}")
        #print(calculateCustomerBillByTypeValue)

# Sample Input 1:
'''
2
regular
30
seasonal
10
3
101
progoti
guwahati
regular
2000
102
parna
maligaon
seasonal
1000
103
Namrata
Delhi
Regular
3000
Seasonal
'''

# Sample Output 1:
'''
1400.0
102 900.0
'''

# Sample Input 2:
'''
2
regular
30
seasonal
10
3
101
progoti
guwahati
daily
2000
102
parna
maligaon
seasonal
1000
103
Namrata
Delhi
Regular
3000
Daily
'''

# Sample Output 2:
'''
Customer Type Not Found.
Customer Not Found.
'''