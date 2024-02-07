

# k = round(4 / 3, 7)
import numpy as np
import math
pi = math.pi
# V0 = round(k * pi * (R ** 3), 7)

# Vextra = ((2 * R) ** 2) - V0

# print(V, V0, round((V0 - V) / pi, 7))

# a = 1
# b = - 3 * R
# c = 0
# d = V * 3 / pi

# p = -b / 3 * a
# q = (p ** 3) + (b * c - 3 * a * d) / (6 * a ** 2)
# r = c / 3 * a

# common = (q ** 2 + ((r - p ** 2) ** 3)) ** (1 / 2)
# first = (q + common) ** (1 / 3)
# second = (q - common) ** (1 / 3)

# h = first + second + p
# poly = np.poly1d([a, b, c, d])
# roots = list(poly.roots)

# print(h / 2)
# for root in roots:
#     if root <= 2 * R and root >= 0:
#         num = round(root.real, 8)
#         print(num)


pi = round(math.pi, 7)
R = round(9.4101888, 7)
V = round(2526.5557948, 7)

a = round(1.0, 7)
b = round(-3.0 * R, 7)
c = round(0.0, 7)
d = round(round(V * 3.0, 7) / pi, 7)

poly = np.poly1d([a, b, c, d])

for root in poly.roots:
    if root <= 2 * R and root >= 0:
        num = round(root.real, 7)
print(num)
