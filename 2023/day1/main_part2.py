import re

from unicodedata import name


with open('day1/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.strip() for line in file.readlines()]

# word2number = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:'eight', 9:"nine"}
digits = {k: v for v in "123456789" for k in [v, name(v).removeprefix('DIGIT ').lower()]}

sum = 0
for line in lines:
    matches = [
                (m.start(1), m.end(1), m.group(1))
                for m in re.finditer(rf"(?=({'|'.join(digits)}))", line)
            ]
    a = matches[0][2]
    b = matches[-1][2]
    print(a, b)
    ab = int(digits[a] + digits[b])
    sum += ab

# Print the list of lines
# print(lines)
print(sum)