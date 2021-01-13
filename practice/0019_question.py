d = 42.195 # km
R = []

inp = input("Enter the distances covered by racers in the marathon (km) \n(Press 'q' to terminate):\n")

while inp != 'q':
    inp = float(inp)

    if inp <= 0.0:
        print("Invalid Input!")
        break
    elif inp > 0.0 and inp != d:
        R.append(inp)
    inp = input()

R.sort()
R.reverse()

Q = []

for i in range(0, 3):
    Q.append(R[i])

print("Highest Distance excluding Finishers:")
print(Q)

'''
QUESTION: 

A marathon is a long-distance race with an official distance of 42.195 kilometre s (26 miles 385 yards), usually run as a road race or footrace.

A local marathon was organized at Bavdhan, Pune. The distance actually covered by the participants has been recorded in an array R[] which is an integer array holding the values in kilometres. If there are N number of participants who started running at a particular time, then the size ofR is N. The participants should cover a distance more than 0.0 km to get recorded in array R[]. 

Find the maximum distances covered by 3 highest racers excluding finishers. If there are only one or nvo racers excluding finishers, give their distances covered. 

R[] will be Input float array. Write a code to take Input array R[], and return 3 maximum distances excluding Finishing Distance d, d = 42.195 km.

SAMPLE INPUT:
42.195
42.195 
42.195
33.25
40
41.2
38.9
37.5 
q 

SAMPLE OUTPUT:
Highest Distance excluding Finishers: 
[41.2, 40.0, 38.9]
'''