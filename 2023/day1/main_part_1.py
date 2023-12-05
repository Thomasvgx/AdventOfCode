with open('day1/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.strip() for line in file.readlines()]

sum = 0
for line in lines:
    nbs = []
    for char in line:
        if char.isdigit():
            nbs.append(char)
    sum += int(nbs[0] + nbs[-1])
# Print the list of lines
print(lines)
print(sum)