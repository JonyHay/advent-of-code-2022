
number_of_knots = 10
knots = [[0, 0] for i in range(number_of_knots)]

tail_positions = set()

def touching(knot1, knot2):
    x = abs(knot1[0] - knot2[0])
    y = abs(knot1[1] - knot2[1])
    return x <= 1 and y <= 1

for line in open('09_rope_bridge/input.txt', 'r').readlines():
    direction = line[0:1]
    amount = int(line[2:].strip())
    for i in range(amount):
        # Move the head
        if direction == "L":
            knots[0][0] -= 1
        elif direction == "R":
            knots[0][0] += 1
        elif direction == "U":
            knots[0][1] += 1
        elif direction == "D":
            knots[0][1] -= 1

        # Move the trailing knots
        for i in range(1, number_of_knots):
            if not touching(knots[i - 1], knots[i]):
                if knots[i - 1][0] > knots[i][0]:
                    knots[i][0] += 1
                elif knots[i - 1][0] < knots[i][0]:
                    knots[i][0] -= 1
                if knots[i - 1][1] > knots[i][1]:
                    knots[i][1] += 1
                elif knots[i - 1][1] < knots[i][1]:
                    knots[i][1] -= 1

        # Add the tail to the set
        tail_positions.add((knots[number_of_knots - 1][0], knots[number_of_knots - 1][1]))

print(len(tail_positions))
