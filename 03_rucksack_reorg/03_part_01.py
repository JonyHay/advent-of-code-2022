# Letters have priorities:
priorities = {}
index = 1
for score in list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))):
    priorities[score] = index
    index += 1

priority_sum = 0
badge_sum = 0

group_rucksacks = []
for input in open('input.txt', 'r').readlines():
    input_length = int(len(input.strip()) / 2)
    in_both = set(input[0:input_length]).intersection(set(input[input_length:]))
    for letter in in_both:
        priority_sum += priorities[letter]
    # Part 2:
    group_rucksacks.append(input.strip())
    if group_rucksacks.__len__() == 3:
        common = set(group_rucksacks[0]).intersection(set(group_rucksacks[1])).intersection(set(group_rucksacks[2]))
        badge_sum += priorities[common.pop()]
        group_rucksacks = []

print("Priority sum: {}".format(priority_sum))
print("Badge sum: {}".format(badge_sum))
