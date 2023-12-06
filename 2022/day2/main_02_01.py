import collections
import math

with open('2022/day2/input.txt', 'r') as file:
    s = [line.rstrip('\n') for line in file.readlines()]

# A = Rock, B = Paper, C = Scissors 1 + 2 + 3
# X = Rock, Y = Paper, Z = Scissors 0 + 3 + 6
strat = {'X': 1, 'Y': 2, 'Z': 3}
score = 0
for game in s:
    your, mine = game.split(' ')
    score += strat[mine]
    if (your == 'A' and mine == 'X') or (your == 'B' and mine == 'Y')\
        or (your == 'C' and mine == 'Z'):
        score += 3
    elif (your == 'A' and mine == 'Y') or (your == 'B' and mine == 'Z')\
        or (your == 'C' and mine == 'X'):
        score += 6
    else:
        score += 0

print(score)