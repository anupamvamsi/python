import random
import queue

# number of data points in one hour (1 data point every millisecond)
n = 3600000

# temperature decreasing
# temp = queue.PriorityQueue()
# for i in range(n-1, 0, -1):
#     temp.put(-i)    # puts temps in descending order

# print(-temp.get())  # prints 3599999 (removes and returns max with correct sign)
# print(-temp.get())  # prints 3599998

# # temperature increasing
# temp = queue.PriorityQueue()
# for i in range(n):
#     temp.put(-i)    # puts temps in descending order

# print(-temp.get())  # prints 3599999
# print(-temp.get())  # prints 3599998


temp = dict()


time = 0.0
for i in range(5):
    time = i * 0.001
    temp[time] = random.uniform(25, 30)

print(temp)
