lst = [4, 7, 9, 8]

# output 4 11 20 28
sum_elements = []
sum_e = 0
for num in lst:
    sum_e += num
    sum_elements.append(sum_e)
print(sum_elements)

i = int(input())
j = int(input())

sum_bw_elements = sum_elements[j-1] - \
    sum_elements[i-2] if i > 1 else sum_elements[j-1]


print(sum_bw_elements)
