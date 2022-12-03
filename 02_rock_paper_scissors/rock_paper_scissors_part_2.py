scoring = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

to_win_mapping = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

to_lose_mapping = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

total_score = 0

for line in open('input.txt', 'r').readlines():
    opponent = line[0]
    outcome = line[2]
    if outcome == "Y": # Draw
        total_score += 3 + scoring[opponent]
    elif outcome == "X": # I must lose
        my_choice = to_lose_mapping[opponent]
        total_score += 0 + scoring[my_choice]
    else: # I must win
        my_choice = to_win_mapping[opponent]
        total_score += 6 + scoring[my_choice]

print("My score is ", total_score)



