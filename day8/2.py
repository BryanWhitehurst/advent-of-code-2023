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
        starting_nodes.append([key, 0])
    
    node_dict[key] = [val1, val2]

#get num steps to Z for each starting node
for node in starting_nodes:
    step_count = 0
    cur_node = node[0]
    i = 0
    while(True):
        if i == len(instructions):
            i = 0
        
        if instructions[i] == 'L':
            cur_node = node_dict[cur_node][0]
        else:
            cur_node = node_dict[cur_node][1]
        
        step_count += 1
        if cur_node[2] == 'Z':
            node[1] = step_count
            break
        i += 1

print(starting_nodes)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

result_lcm = starting_nodes[0][1]
for node in starting_nodes[1:]:
    result_lcm = lcm(result_lcm, node[1])

print(result_lcm)