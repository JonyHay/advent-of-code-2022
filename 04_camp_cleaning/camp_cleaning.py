
fully_overlapping = 0
just_overlaps = 0

for input in open('input.txt', 'r').readlines():
    pair = input.strip().split(",")
    a1 = [int(x) for x in pair[0].split("-")]
    a2 = [int(x) for x in pair[1].split("-")]
    # Part 2
    if len(set(range(a1[0], a1[1] + 1)).intersection(set(range(a2[0], a2[1] + 1)))) > 0:
        just_overlaps += 1
        # Part 1
        if a1[0] <= a2[0] <= a2[1] <= a1[1] or a2[0] <= a1[0] <= a1[1] <= a2[1]:
            fully_overlapping += 1

print("There are {} fully overlapping and {} slightly overlapping assignments".format(fully_overlapping, just_overlaps))

