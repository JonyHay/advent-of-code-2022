
SAME_INT_CHECK_NEXT = 2
CORRECT_CHECK_NEXT = 2

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

    if is_integer(part1) and is_integer(part2):        
        p1_int = int(part1)
        p2_int = int(part2)
        if p1_int < p2_int:
            return ORDER_CORRECT
        elif p1_int > p2_int :
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
            return ORDER_CORRECT
        elif len(list1) > 0 and len(list2) == 0:
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
                return ORDER_WRONG
            elif x >= len(list1) and x < len(list2):  # If the left list runs out of items first, the inputs are in the right order.
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


lines = []
for line in open('./13_distress_signal/input.txt', 'r').readlines():
    clean = line.strip()
    if len(clean) > 0:
        lines.append(clean)

lines.append("[[2]]")
lines.append("[[6]]")

# Sort all lines using compare method
from functools import cmp_to_key
lines = sorted(lines, key=cmp_to_key(compare), reverse=True)

div0 = 0
div1 = 0
for index in range(len(lines)):
    print(lines[index])
    if lines[index] == "[[2]]":
        div0 = index + 1
    elif lines[index] == "[[6]]":
        div1 = index + 1

sum = div0 * div1
print("Decoder key: ", sum)
