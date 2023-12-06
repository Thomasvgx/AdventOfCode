import collections
import math

with open('2022/day2/input.txt', 'r') as file:
    s = [line.rstrip('\n') for line in file.readlines()]

# A = Rock, B = Paper, C = Scissors 1 + 2 + 3
# X = Loss, Y = Draw, Z = Win 0 + 3 + 6
strat = {'X': 1, 'Y': 2, 'Z': 3}
strat2 = {'A': 1, 'B': 2, 'C': 3}
win = {'A':'Y', 'B':'Z', 'C':'X'}
loss = {'A':'Z', 'B':'X', 'C':'Y'}

score = 0
for game in s:
    your, mine = game.split(' ')
    if mine == 'Y': # Draw
        score += 3 + strat2[your]
    elif mine == 'X': # Loss
        score += 0 + strat[loss[your]]
    elif mine == "Z": # Win
        score += 6 + strat[win[your]]

print(score)
