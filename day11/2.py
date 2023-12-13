import sys
import math
f = open("input.txt", "r")
#read input into 2d array
lines = f.readlines()

galaxies  = []

rows = [] 
for i in range(len(lines)):
    galaxy_found = False
    for j in range(len(lines[0]) - 1):
        if lines[i][j] == '#':
            galaxy_found = True
    if not galaxy_found:
        rows.append(i)
    

cols = []
#get row index that doubles
for i in range(len(lines[0]) - 1):
    galaxy_found = False
    for j in range(len(lines)):
        if lines[j][i] == '#':
            galaxy_found = True
    
    if not galaxy_found:
        cols.append(i)

x = rows.pop(0)
x_space = 0
for i in range(len(lines)):
    if i >= x:
        if len(rows) != 0: x = rows.pop(0)
        else: x = sys.maxsize
        x_space += 999999
    
    y_space = 0 
    cols_copy = cols.copy()
    y = cols_copy.pop(0)
    for j in range(len(lines[0]) - 1):

        if j >= y:
            if len(cols_copy) != 0: y = cols_copy.pop(0)
            else: y = sys.maxsize
            y_space += 999999

        if lines[i][j] == '#':
            galaxies.append([i + x_space, j + y_space])
                    
total = 0
strt = 0 
for i in range(len(galaxies)):
    for j in range(strt, len(galaxies)):

        if galaxies[i] == galaxies[j]:
            continue
        x1 = galaxies[i][0]
        y1 = galaxies[i][1]

        x2 = galaxies[j][0]
        y2 = galaxies[j][1]
        
        distance = abs((x2 - x1)) + abs((y2 - y1))
        
        if distance > 0: 
            total += distance
    strt  += 1 

print(total)
