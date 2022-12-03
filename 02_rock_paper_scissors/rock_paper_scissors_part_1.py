mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

total_score = 0

for line in open('input.txt', 'r').readlines():
    opponent = mapping[line[0]]
    me = mapping[line[2]]
    outcome = opponent - me
    if outcome == -2 or outcome == 1: # Opponent Wins
        total_score += me
    elif outcome == -1 or outcome == 2: # I win
        total_score += me + 6
    else: # Draw
        total_score += me + 3

print("My score is ", total_score)
