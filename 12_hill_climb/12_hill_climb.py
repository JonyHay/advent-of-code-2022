import math

def print_map(map):
    for y in range(len(map[0])):
        for x in range(len(map)):
            if map[x][y] == None:
                print(".", end='')
            else:
                print(map[x][y], end='')
        print()

heightmap = None
start = None
end = None

for line in open('12_hill_climb/input.txt', 'r').readlines():
    x = 0
    if heightmap == None:
        heightmap = [[] for i in range(len(line.strip()))]
    for s in list(line.strip()):
        if s == "S":
            start = (x, len(heightmap[x]))
        elif s == "E":
            end = (x, len(heightmap[x]))
        heightmap[x].append(s)
        x += 1
     
width = len(heightmap)
height = len(heightmap[0])

graph = {}


def letter_score(n):
    if n == 'S':
        return ord('a')
    if n == 'E':
        return ord('z')
    return ord(n)

def get_height(x, y):
    return letter_score(heightmap[x][y])

def move_between(x1, y1, x2, y2):
    a = get_height(x1, y1)
    b = get_height(x2, y2)
    if a >= b:
        return True
    return b == a + 1


source = None
destination = None
neighbs = 0
for y in range(height):
    for x in range(width):
        index = "{},{}".format(x, y)
        graph[index] = []
        # Look Left
        if x > 0 and move_between(x, y, x - 1, y):
            graph[index].append("{},{}".format(x - 1, y))
            neighbs += 1
        # Look Right
        if x < (width - 1) and move_between(x, y, x + 1, y):
            graph[index].append("{},{}".format(x + 1, y))
            neighbs += 1
        # Look Up
        if y > 0 and move_between(x, y, x, y - 1):
            graph[index].append("{},{}".format(x, y - 1))
            neighbs += 1
        # Look Down
        if y < (height - 1) and move_between(x, y, x, y + 1):
            graph[index].append("{},{}".format(x, y + 1))
            neighbs += 1 
        if heightmap[x][y] == "S":
            source = index
        if heightmap[x][y] == "E":
            destination = index

################################# ALL GOOD SO FAR

print("Find route from {} to {}".format(source, destination))

# Initialise

dist = {}
prev = {}
queue = []
seen = []

for node in graph.keys():
    dist[node] = math.inf
    prev[node] = {}
    queue.append(node)
dist[source] = 0


while (queue): # Queue is not empty
    print("Queue Size = ", len(queue))

    # Find U - the vertex in Q with min dist[u]
    u = queue[0]
    for j in queue:
        if dist[j] < dist[u]:
            u = j
    print("Look at", u)
    seen.append(u)

    # Remove U from queue
    queue.pop(queue.index(u))

    # For each neighbour V of U still in Q
    # Set of X not in Y
    neighbours = graph[u]
    for v in neighbours:
        print(" - Neighbour", v)
        if v not in seen:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    print()


print(dist[destination])
