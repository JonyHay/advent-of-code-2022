ORDER_CORRECT = 1
ORDER_WRONG = -1
ORDER_SAME = 0
INTEGER = 0
LIST = 1

def get_type(t):
    if t.startswith("["):
        return LIST
    else:
        return INTEGER

def is_integer(t):
    return get_type(t) == INTEGER

def is_list(t):
    return get_type(t) == LIST    

def print_ws(depth):
    for x in range(depth):
        print(" ", end = '')

def compare(part1, part2, depth = 0):
    print_ws(depth)
    print("- Compare {} vs {}".format(part1, part2))

    if is_integer(part1) and is_integer(part2):        
        p1_int = int(part1)
        p2_int = int(part2)
        if p1_int < p2_int:
            print_ws(depth)
            print("- Left side is smaller, so inputs are in the right order")
            return ORDER_CORRECT
        elif p1_int > p2_int :
            print_ws(depth)
            print("- Right side is smaller, so inputs are not in the right order")
            return ORDER_WRONG
        else:
            return ORDER_SAME
    elif is_integer(part1) and is_list(part2):
        return compare("[" + part1 + "]", part2, depth + 1)
    elif is_list(part1) and is_integer(part2):
        return compare(part1, "[" + part2 + "]", depth + 1)
    else: # Handle pure lists        
        list1 = read_values(part1)
        list2 = read_values(part2)

        # Empty lists
        if len(list1) == 0 and len(list2) > 0:
            print_ws(depth)
            print("- Empty left list, so inputs are in the right order")
            return ORDER_CORRECT
        elif len(list1) > 0 and len(list2) == 0:
            print_ws(depth)
            print("- Empty right list, so inputs are not in the right order")
            return ORDER_WRONG

         # Compare the first value of each list, then the second, etc ...
        for x in range(max(len(list1), len(list2))):
            # If both lists have values
            if x < len(list1) and x < len(list2):
                r = compare(list1[x], list2[x], depth + 1) # do what with the result?
                if r == ORDER_WRONG:
                    return ORDER_WRONG
                elif r == ORDER_CORRECT:
                    return ORDER_CORRECT
            elif x < len(list1) and x >= len(list2): # If the right list runs out of items first, the inputs are not in the right order
                print_ws(depth)
                print("- Right side ran out of items, so inputs are not in the right order")
                return ORDER_WRONG
            elif x >= len(list1) and x < len(list2):  # If the left list runs out of items first, the inputs are in the right order.
                print_ws(depth)
                print("- Left side ran out of items, so inputs are in the right order")
                return ORDER_CORRECT
            else:
                print("ERROR, CANNOT HANDLE")
        return ORDER_SAME
     

def read_values(list, start = 1):
    start = 1
    end = 2
    mode = 0
    v = ""
    values = []
    while end <= len(list):        
        l = list[start:end]
        if l == "[": # We go deeper!
            mode += 1
            v = v + "["
        elif l == "]" and mode > 0:
            mode -= 1
            v = v + "]"
        elif l == "," and mode == 0:
            values.append(v)
            v = ""
        elif end == len(list):
            if len(v) > 0:
                values.append(v)
            v = ""
        else:
            v = v + l 
        start += 1
        end += 1
    return values


# Parse the input
part1 = None
part2 = None
index = 1
correct = []
for line in open('./13_distress_signal/input.txt', 'r').readlines():
    if not part1:
        part1 = line.strip()
    elif not part2:
        part2 = line.strip()
        print("== Pair {} ==".format(index))
        r = compare(part1, part2)
        print()
        if r == 1:
            correct.append(index)
    else:
        part1 = None
        part2 = None
        index +=1

sum = 0
for i in correct:
    sum += i

print("Sum of correct incides: {}".format(sum))
