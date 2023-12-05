with open('day2/input.txt', 'r') as file:
    # Read all lines into a list
    lines = [line.strip() for line in file.readlines()]

sum = 0

for line in lines:
    current_id = line.split(":")[0].removeprefix('Game ')
    # print(current_id)
    sets = line.split(": ")[1].split("; ")
    min_b = 0
    min_g = 0
    min_r = 0
    # print(sets)
    for set in sets:
        nbs_balls = set.split(', ')
        # print(nbs_balls)
        for nb_balls in nbs_balls:
            if 'red' in nb_balls:
                if (n := int(nb_balls.split(" ")[0])) > min_r:
                    min_r = n
            if 'green' in nb_balls:
                if (n := int(nb_balls.split(" ")[0])) > min_g:
                    min_g = n
            if 'blue' in nb_balls:
                if (n := int(nb_balls.split(" ")[0])) > min_b:
                    min_b = n
    sum += (min_b * min_g * min_r)

print(sum)