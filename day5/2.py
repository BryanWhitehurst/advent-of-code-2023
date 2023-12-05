import sys
f = open("input.txt", "r")

lines = f.readlines()

seeds = lines[0].split(': ')[1].strip().split()
seeds = list(map(lambda x: int(x), seeds))

list_of_maps = []
cur_rows = []
i = 3
while i < len(lines): 
    if lines[i] == '\n':
        list_of_maps.append(cur_rows)
        cur_rows = []
        i += 2
        continue
    
    cur_rows.append(list(map(lambda x: int(x), lines[i].strip().split())))
    i += 1

    if i == len(lines):
        list_of_maps.append(cur_rows)

def getMappedValue(rows, val):
    for row in rows:
        if val >= row[1] and val <= row[1] + row[2]:
            return row[0] + val - row[1]
    return val

final_val = sys.maxsize
i = 0
while i < len(seeds):
    for j in range(seeds[i], seeds[i] + seeds[i + 1]):
        cur_val = j
        for map in list_of_maps:
            cur_val = getMappedValue(map, cur_val)

        final_val = min(cur_val, final_val)
    i += 2
print(final_val)