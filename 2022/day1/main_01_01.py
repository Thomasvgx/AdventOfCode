import collections
import math

with open('2022/day1/input.txt', 'r') as file:
    s = [line.rstrip('\n') for line in file.readlines()]

sum = [0]
i = 0
for element in s:
    if element != '':
        sum[i] = sum[i] + int(element)
    else:
        sum.append(0)
        i += 1

print(max(sum))
