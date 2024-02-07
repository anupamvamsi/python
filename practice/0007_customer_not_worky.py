class Customer:
    def __init__(self,orderId,customerName,address,customerType,orderAmount):
        self.orderId = orderId
        self.customerName = customerName
        self.address = address
        self.customerType = customerType
        self.orderAmount = orderAmount
class Store:
    def __init__(self,customerTypeIncentive,customerList):
        self.customerTypeIncentive = customerTypeIncentive
        self.customerList = customerList
    def calculateBill(self,customerOb):
        if customerOb.customerType.casefold() not in self.customerTypeIncentive:
            return None
        else:
            finalBill = 0
            discountedBill = customerOb.orderAmount * self.customerTypeIncentive[customerOb.customerType.casefold()] / 100
            finalBill = customerOb.orderAmount - discountedBill
            return finalBill
    def calculateCustomerBillByType(self,customerType):
        if customerType.casefold() not in self.customerTypeIncentive:
            return None
        else:
            out_ = {}
            for i in self.customerList:
                if i.customerType.casefold() == customerType.casefold():
                    out_[i.orderId] = i.orderAmount - (i.orderAmount * self.customerTypeIncentive[customerType.casefold()] / 100)
            if out_ == {}:
                return None
            else:
                return out_

if __name__ == "__main__":
    customerTypeIncentive = {}
    for _ in range(int(input())):
        ctype = input().casefold()
        discountper = int(input())
        customerTypeIncentive[ctype] = discountper
    customerList = []
    for _ in range(int(input())):
        orderId = int(input())
        customerName = str(input())
        address = str(input())
        customerType = str(input())
        orderAmount = int(input())
        custObj = Customer(orderId,customerName,address,customerType,orderAmount)
        customerList.append(custObj)
    storeOb = Store(customerTypeIncentive,customerList)
    customerType = input()
    temp = storeOb.calculateBill(customerList[0])
    if temp is None:
        print('Customer Type Not Found.')
    else:
        print(temp)
    temp = storeOb.calculateCustomerBillByType(customerType)
    if temp is None:
        print('Customer Not Found.')
    else:
        for i in temp:
            print(i,temp[i])

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
103 
Namrata
Delhi
Regular 
3000
'''

# Sample Output 2:
'''
Customer Type Not Found. 
Customer Not Found. 
'''