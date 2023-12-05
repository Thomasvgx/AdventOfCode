r_limit = 12
g_limit = 13
b_limit = 14

with open('day2/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.strip() for line in file.readlines()]

sum = 0

for line in lines:
    flag = True
    current_id = line.split(":")[0].removeprefix('Game ')
    # print(current_id)
    sets = line.split(": ")[1].split("; ")
    # print(sets)
    for set in sets:
        nbs_balls = set.split(', ')
        print(nbs_balls)
        for nb_balls in nbs_balls:
            if 'red' in nb_balls:
                if int(nb_balls.split(" ")[0]) > r_limit:
                    flag = False
            if 'green' in nb_balls:
                if int(nb_balls.split(" ")[0]) > g_limit:
                    flag = False
            if 'blue' in nb_balls:
                if int(nb_balls.split(" ")[0]) > b_limit:
                    flag = False
    if flag == True:
        sum += int(current_id)

    

# 12 red cubes, 13 green cubes, and 14 blue cubes

print(sum)