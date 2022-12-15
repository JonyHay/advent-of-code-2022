


def print_map(map):
    for y in range(0, map_bound_y_upper + 3):
        for x in range(map_bound_x_lower - 15, map_bound_x_upper + 15):
            if x == 500 and y == 0:
                print("+", end='')
            elif y == floor_y:
                print("#", end='') 
            elif x >= len(map) or y >= len(map[0]):
                print(".", end='')    
            elif map[x][y] == None:
                print(".", end='')
            else:
                print(map[x][y], end='')
        print()

def parse_point(txt):
    txt = txt.strip()
    s = txt.split(",")
    return (int(s[0]), int(s[1]))

def parse_points(txt):
    s = txt.split("->")
    ps = []
    for p in s:
        ps.append(parse_point(p))
    return ps


lines = []
map_bound_x_lower = 999
map_bound_x_upper = 0
map_bound_y_lower = 999
map_bound_y_upper = 0
for line in open('14_regolith_reservoir/input.txt', 'r').readlines():
    points = parse_points(line)
    # Find bounds
    for point in points:
        if point[0] < map_bound_x_lower:
            map_bound_x_lower = point[0]
        if point[0] > map_bound_x_upper:
            map_bound_x_upper = point[0]
        if point[1] < map_bound_y_lower:
            map_bound_y_lower = point[1]
        if point[1] > map_bound_y_upper:
            map_bound_y_upper = point[1]
    # Add lines to array
    for x in range(len(points) - 1):
        lines.append((points[x], points[x + 1]))

# Print map bounds
print("Map Bounds: {},{} -> {},{}".format(map_bound_x_lower, map_bound_y_lower, map_bound_x_upper, map_bound_y_upper))
floor_y = map_bound_y_upper + 2
print("Map Floor:", floor_y)

# Draw lines on map
map = [["." for i in range(map_bound_y_upper + 3)] for i in range(map_bound_x_upper + 1000)]
for line in lines:
    start_x = min(line[0][0], line[1][0])
    start_y = min(line[0][1], line[1][1])
    end_x = max(line[0][0], line[1][0])
    end_y = max(line[0][1], line[1][1])
    if start_x == end_x:
        for y in range(start_y, end_y + 1):
            map[start_x][y] = "#"
    elif start_y == end_y:
        for x in range(start_x, end_x + 1):
            map[x][start_y] = "#"

# Create unit of sand at source
sand_counter = 0
for x in range(100000): # We have to have some limits

    sand = (500, 0)
    while (True):

        # Remove the map change
        map[sand[0]][sand[1]] = "."

        # Can move?
        newsand = sand

        try:
            if map[sand[0]][sand[1] + 1] == "." and (sand[1] + 1) < floor_y : # Straight down?
                newsand = (sand[0], sand[1] + 1)
            elif map[sand[0] - 1][sand[1] + 1] == "." and (sand[1] + 1) < floor_y : # Down left?
                newsand = (sand[0] - 1, sand[1] + 1)
            elif map[sand[0] + 1][sand[1] + 1] == "." and (sand[1] + 1) < floor_y : # Down left?
                newsand = (sand[0] + 1, sand[1] + 1)
        except Exception as e:
            print("Error moving from {} on sand {}:".format(sand, x), e)
            raise e

        # Error handling
        if newsand[0] < 0 or newsand[0] > len(map):
            print("Pos outside bounds:",newsand)
            exit(0)

        if sand[0] == newsand[0] and sand[1] == newsand[1]: # no change!
            map[sand[0]][sand[1]] = "o"

            if sand[0] == 500 and sand[1] == 0:
                map[sand[0]][sand[1]] = "o"
                print_map(map)
                print(sand_counter + 1)            
                exit(0)

            break
        else:
            sand = newsand

        # Update the map again
        map[sand[0]][sand[1]] = "o"

    sand_counter += 1 # Update once settled

    #print_map(map)
    #print()

print_map(map)





