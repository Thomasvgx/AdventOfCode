with open('day4/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.rstrip('\n') for line in file.readlines()]

lines = [line.split(' | ') for line in lines]

lines = [val.split(" :")[-1] for sublist in lines for val in sublist]

lines = [lines[i:i+2] for i in range(0, len(lines), 2)]

curated_input = []
for index, line in enumerate(lines):
    id = int(line[0].split(': ')[0].removeprefix("Card "))
    tirage =   [int(num) for num in line[0].split(': ')[1].split()]
    # line[0].split(': ')[1]
    main = [int(num) for num in line[1].split()]
    
    curated_input.append([id, tirage, main])
    # lines[index].append([int(num) for num in line[0].split()])
    # lines[index].append([int(num) for num in line[1].split()])

print(curated_input[0])
sum = 0
from collections import defaultdict
scratch_cards = defaultdict(int)

for index, line in enumerate(curated_input):
    sum += 1
    scratch_cards[index] += 1
    nb = len(set(line[1]).intersection(set(line[2])))
    print(set(line[1]).intersection(set(line[2])))
    for i in range(nb):
        scratch_cards[index + i + 1] += scratch_cards[index]
        print(scratch_cards)
    sum += scratch_cards[index] -1 

print(sum)