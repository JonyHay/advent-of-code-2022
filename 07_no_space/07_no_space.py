
filesystem = {"name": "/", "typ": "dir", "children": {}, "parent": None}
current_dir = None

# Load the Filesytem
for line in open('input.txt', 'r').readlines():    
    if line.startswith("$"):
        command = line[2:4]        
        if command == "cd":
            parameter = line[5:].strip()
            # Navigate relative to the current directory
            if parameter == "/":
                current_dir = filesystem
            elif parameter == "..":                
                current_dir = current_dir["parent"]
            else:
                # Create a new dir object
                current_dir = current_dir["children"][parameter]
    else: # Handling Output
        if line.startswith("dir"): # Add a dir to the model
            dir_name = line[4:].strip()
            new_dir = {"name": dir_name, "typ": "dir", "children": {}, "parent": current_dir}
            current_dir["children"][dir_name] = new_dir
        else:
            segments = line.split(" ")
            current_dir["children"][segments[1].strip()] = {"name": segments[1].strip(), "typ": "file", "size": segments[0], "parent": current_dir}






# Recursively get size function
combined_size = 0
def find_total_size(directory):
    global combined_size
    size = 0
    for sub in directory["children"].values():
        if sub["typ"] == "dir": # Get dir size
            size += find_total_size(sub)
        else: # Add file size to it
            size += int(sub["size"])
    # Add to combined size counter
    if size <= 100000:
        combined_size += size
    return size

total_disk_space = 70000000
required_disk_space = 30000000
used_disk_space = find_total_size(filesystem)
print("Part 1 size: ", combined_size)

# Disk space to find 
to_find = used_disk_space - (total_disk_space - required_disk_space)
print("Need to free up ", to_find)

# Find the smallest directory on the filesystem that is BIGGER than to_find
small_dirs = []
def find_small_dirs(directory, min_size):
    global small_dirs
    my_size = find_total_size(directory)
    if my_size >= min_size:
        small_dirs.append(my_size)
    for sub in directory["children"].values():
        if sub["typ"] == "dir": # Get dir size
            find_small_dirs(sub, min_size)

find_small_dirs(filesystem, to_find)
small_dirs.sort()
print(small_dirs.pop(0))

