with open('day4/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.rstrip('\n') for line in file.readlines()]

lines = [line.split(' | ') for line in lines]

lines = [val.split(" :")[-1] for sublist in lines for val in sublist]

lines = [lines[i:i+2] for i in range(0, len(lines), 2)]

for index, line in enumerate(lines):
    lines[index][0] = line[0].split(': ')[-1]
    lines[index][0] = [int(num) for num in line[0].split()]
    lines[index][1] = [int(num) for num in line[1].split()]

sum = 0

for line in lines:
    pow = 0
    for card_nb in line[0]:
        if card_nb in line[1]:
            pow += 1
    sum += 2**(pow - 1) if pow != 0 else 0

print(sum)