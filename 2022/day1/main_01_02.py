import collections
import math

with open('2022/day1/input.txt', 'r') as file:
    s = [line.rstrip('\n') for line in file.readlines()]

somme = [0]
i = 0
for element in s:
    if element != '':
        somme[i] = somme[i] + int(element)
    else:
        somme.append(0)
        i += 1
print(sum(sorted(somme)[-3:]))