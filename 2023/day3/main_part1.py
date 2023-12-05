with open('day3/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.rstrip('\n') for line in file.readlines()]

print(len(lines[0]))

sum = 0
number = []
next_is_nb = True
is_flagged = False
# lines = lines[0]

tab_voisins = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]

def check_if_flag(tab, i, j):
    if i < 0 or j < 0 or i >= len(tab) or j >= len(tab[0]):
        return False
    else:
        return (not tab[i][j].isalnum()) and (tab[i][j] != ".")

for i, line in enumerate(lines):
    number = []
    next_is_nb = False
    for j, char in enumerate(line):
        if char.isdigit():
            if not next_is_nb: 
                number = []
                is_flagged = False
            number.append(char)
            
            for ii, jj in tab_voisins:
                if check_if_flag(lines, i + ii, j + jj):
                    is_flagged = True
            
            if j+1 < len(lines[0]):
                if not lines[i][j+1].isdigit():
                    next_is_nb = False
                    if is_flagged:
                        sum += int("".join(number))
                else:
                    next_is_nb = True
            else: # end of line
                if len(number) > 0 and is_flagged:
                    sum += int("".join(number))

print(sum)
