

sensors = []
beacons = []
ranges = []
map_min_x = None
map_max_x = None
map_min_y = None
map_max_y = None

def print_map(out_of_range = set()):
    if map_max_y - map_min_y > 100: # Do not print wider than console
        return
    for y in range(map_min_y,map_max_y):
        for x in range(map_min_x - 5,map_max_x + 5):
            drawn = False
            for s in sensors:
                if s[0] == x and s[1] == y:
                    print("S", end='')
                    drawn = True
            for b in set(beacons):
                if b[0] == x and b[1] == y:
                    print("B", end='')
                    drawn = True
            if not drawn:
                cell = x,y
                if cell in out_of_range:
                    print("#", end='')
                else:
                    print(".", end='')
        print()


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

print("Map Bounds:",map_min_x, map_max_x, map_min_y, map_max_y)
print("Ranges:", ranges)

# Calculate range set
in_range = set()
#y = 10
#for x in range(map_min_x, map_max_x):
#    # A cell contains no beacon if it is within range of ANY sensor
#    cell = x, y
#    for i, s in enumerate(sensors):
#        if distance(cell, s) <= ranges[i]:
#            in_range.add(cell)

# Alt method
# For Each Sensor:
# Work out all cells within its range
# And if the cell overlaps with the 
for i, sensor in enumerate(sensors):
    print(i, sensor)
    y = 2000000
    sensor_range = ranges[i]
    for x in range(sensor[0] - sensor_range, sensor[0] + sensor_range):
        cell = x, y
        if distance(cell, sensor) <= ranges[i]:
            in_range.add(cell)

# Remove beacons from out_of_range
print("Removing beacon positions from in_range data ...")
for b in set(beacons):
    in_range.discard(b)


print_map(in_range)
print("Positions in range:", len(in_range))
