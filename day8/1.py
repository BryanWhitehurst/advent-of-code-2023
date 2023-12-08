f = open("input.txt", "r")

lines = f.readlines()

instructions = lines[0]
lines = lines[2:]
instructions_dict = {}
for line in lines:
    key, val = line.strip().split(' = ')
    val1, val2 = val.split(',')
    val1 = val1[1:]
    val2 = val2[1:4]

    instructions_dict[key] = [val1, val2]

print(instructions_dict)