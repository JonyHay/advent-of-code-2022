sensors = []
beacons = []
ranges = []
map_min_x = None
map_max_x = None
map_min_y = None
map_max_y = None

# Also updates map bound variables
def extract_coordinates(txt):
    global map_min_x, map_max_x, map_min_y, map_max_y
    point = int(txt[(txt.index("x=") + 2):txt.index(",")]), int(txt[(txt.index("y=") + 2):])
    if map_min_x == None or point[0] < map_min_x:
        map_min_x = point[0]
    if map_max_x == None or point[0] > map_max_x:
        map_max_x = point[0]
    if map_min_y == None or point[1] < map_min_y:
        map_min_y = point[1]
    if map_max_y == None or point[1] > map_max_y:
        map_max_y = point[1]
    return point

# Calculate "Manhattan Distance" between two points
def distance(b1, b2):
    return abs(b2[0] - b1[0]) + abs(b2[1] - b1[1])

# Parse input to sensors[] and beacons[]
for x in [i.strip().split(":") for i in open('15_beacon_exclusion_zone/input.txt', 'r').readlines()]:
    sensors.append(extract_coordinates(x[0]))
    beacons.append(extract_coordinates(x[1]))
    ranges.append(distance(sensors[-1], beacons[-1]))

# Calculate range set
in_range = set()
for i, sensor in enumerate(sensors):
    y = 2000000
    sensor_range = ranges[i]
    for x in range(sensor[0] - sensor_range, sensor[0] + sensor_range):
        cell = x, y
        if distance(cell, sensor) <= ranges[i]:
            in_range.add(cell)

# Remove beacons from out_of_range
print("Removing beacon/sensor positions from in_range data ...")
for b in set(beacons):
    in_range.discard(b)
for s in sensors:
    in_range.discard(s)

print("Positions in range:", len(in_range)) # 5688618

##### PART 2
print()
print("===============================================================")
print()

def check_cell(cell):
    #cells_checked.add(cell)
    if 0 <= cell[0] <= search_bounds and 0 <= cell[1] <= search_bounds:
        for i, s in enumerate(sensors):
            sr = ranges[i]            
            dist = distance(cell, s)
            if dist <= sr:
                return

        print("Winning cell is", cell)
        tun_freq = (cell[0] * 4000000) + cell[1]
        print("Tuning Frequency", tun_freq)
        exit(0)

search_bounds = 4000000
for i, sensor in enumerate(sensors):
    sensor_range = ranges[i]
    my_boundary = set()
    rel_y = 1
    for y in range(sensor[1] - sensor_range - 1, sensor[1] + sensor_range + 2):
        check_cell( ((sensor[0] - rel_y + 1), y))
        check_cell( ((sensor[0] + rel_y - 1), y))
        if y < sensor[1]:
            rel_y += 1
        else:
            rel_y -= 1
    