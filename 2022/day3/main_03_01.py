with open('2022/day3/input.txt', 'r') as file:
    s = [line.rstrip('\n') for line in file.readlines()]

intersection = []
for line in s:
    intersection.append(list(set(line[:len(line)//2]).intersection(line[len(line)//2:])))

sum = 0 

for letter in intersection:
    letter = ''.join(letter)
    sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38

print(sum)

