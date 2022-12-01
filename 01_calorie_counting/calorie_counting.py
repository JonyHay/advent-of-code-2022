

elves = {}
elf = 1
elves[elf] = 0

for input in open('input.txt', 'r').readlines():
    cleaned = input.strip()
    if len(cleaned) == 0:
        elf = elf + 1
        elves[elf] = 0
    else:
        elves[elf] = elves[elf] + int(cleaned)

calorie_values = sorted(list(elves.values()), reverse=True)
print("The most calories an elf has is {}".format(calorie_values[0]))

top_three_calories = calorie_values[0] + calorie_values[1] + calorie_values[2]
print("The top-three-calorie-carriers have {} calories".format(top_three_calories))
