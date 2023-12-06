import sys
from datetime import datetime
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

for seed in seeds:
    cur_val = seed
    for map in list_of_maps:
        cur_val = getMappedValue(map, cur_val)

    final_val = min(cur_val, final_val)

startTime = datetime.now()
for i in range(1000000000):
    1 + 1
print(datetime.now() - startTime)
print(final_val)