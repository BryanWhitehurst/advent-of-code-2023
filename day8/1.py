f = open("input.txt", "r")

lines = f.readlines()

instructions = lines[0].strip()
lines = lines[2:]
node_dict = {}
for line in lines:
    key, val = line.strip().split(' = ')
    val1, val2 = val.split(',')
    val1 = val1[1:]
    val2 = val2[1:4]

    node_dict[key] = [val1, val2]

step_count = 0
cur_node = 'AAA'
i = 0
while(True):
    if i == len(instructions):
        i = 0
    
    if instructions[i] == 'L':
        cur_node = node_dict[cur_node][0]
    else:
        cur_node = node_dict[cur_node][1]
    
    step_count += 1
    if cur_node == 'ZZZ':
        break
    i += 1

print(step_count)


 
