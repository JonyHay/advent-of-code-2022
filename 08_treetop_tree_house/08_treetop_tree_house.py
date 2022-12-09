# I really wanted the forest represented as an X/Y 2d array, i.e. forest[x][y]

def output_forest(forest):
    for y in range(len(forest[0])):
        for x in range(len(forest)):
            print(forest[x][y], end='')
        print()

forest = None

for line in open('08_treetop_tree_house/input.txt', 'r').readlines():
    x = 0
    if forest == None:
        forest = [[] for i in range(len(line.strip()))]
    for tree in list(line.strip()):
        forest[x].append(int(tree))
        x += 1
     
width = len(forest)
height = len(forest[0])

# Mark interior trees as visible
visible = [[0 for i in range(height)] for i in range(width)]

def find_visible(width_range, height_range, direction):
    global visible
    if direction == "x":
        for x in width_range: # We process for each row
            height_so_far = -1
            for y in height_range:
                if forest[x][y] > height_so_far:
                    visible[x][y] = 1
                    height_so_far = forest[x][y]
    else:
        for y in height_range:
            height_so_far = -1
            for x in width_range:
                if forest[x][y] > height_so_far:
                    visible[x][y] = 1
                    height_so_far = forest[x][y]

find_visible(range(width), range(height), "x")
find_visible(range(width), range(height - 1, 0, -1), "x")
find_visible(range(width), range(height), "y")
find_visible(range(width - 1, 0, -1), range(height), "y")

# Count visible trees
count = 0
for x in range(width):
    for y in range(height):
        if visible[x][y] == 1:
            count += 1

print("There are {} visible trees".format(count))

# PART 2 - SCENERY
def get_scenic_score(x, y):
    look_up = 0
    for look_y in range(y - 1, -1, -1):
        look_up += 1
        if forest[x][look_y] >= forest[x][y]:
            break
    look_down = 0
    for look_y in range(y + 1, height):
        look_down += 1
        if forest[x][look_y] >= forest[x][y]:
            break
    look_right = 0
    for look_x in range(x + 1, width):
        look_right += 1
        if forest[look_x][y] >= forest[x][y]:
            break
    look_left = 0
    for look_x in range(x - 1, -1, -1):
        look_left += 1
        if forest[look_x][y] >= forest[x][y]:
            break    
    return look_up * look_down * look_right * look_left


best_scenic_score = 0
for x in range(width):
    for y in range(height):     
        score_here = get_scenic_score(x, y)
        if score_here > best_scenic_score:
            best_scenic_score = score_here      


print("The best scenic score is {}".format(best_scenic_score))        
