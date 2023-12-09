f = open("input.txt", "r")

lines = f.readlines()

instructions = lines[0].strip()
lines = lines[2:]
node_dict = {}
starting_nodes = []

for line in lines:
    key, val = line.strip().split(' = ')
    val1, val2 = val.split(',')
    val1 = val1[1:]
    val2 = val2[1:4]
    if key[2] == 'A':
        starting_nodes.append(key)
    
    node_dict[key] = [val1, val2]

step_count = 0
i = 0
allZZZ = True
while(True):
    new_nodes = []
    
    if i == len(instructions):
        i = 0

    while(len(starting_nodes) > 0):
        cur_node = starting_nodes.pop()

        if instructions[i] == 'L':
            new_nodes.append(node_dict[cur_node][0])
            if node_dict[cur_node][0][2] != 'Z': allZZZ = False
        else:
            new_nodes.append(node_dict[cur_node][1])
            if node_dict[cur_node][1][2] != 'Z': allZZZ = False
    
    step_count += 1
    if allZZZ:
        break

    allZZZ = True
    starting_nodes = new_nodes.copy()
    print(new_nodes)
    new_nodes = []
    i += 1

print(step_count)