f = open("input.txt", "r")

lines = f.readlines()
symbol_locations = []
total = 0

for i in range(len(lines)):
    for j in range(len(lines[0]) -1):
        #if symbol found, add to symbol list
        if (not lines[i][j].isdigit()) and (not lines[i][j] == '.'):
            symbol_locations.append((i, j))

gear_dict = {}
for i in range(len(lines)):
    cur_num = ''
    numFound = False
    gear_list = set()

    for j in range(len(lines[0]) - 1):
        if lines[i][j].isdigit():
            cur_num += lines[i][j]
            numFound = True

            #check if adjacent to symbol
            if (i, j + 1) in symbol_locations:
                gear_list.add((i, j + 1))
            if (i, j - 1) in symbol_locations:
                gear_list.add((i, j - 1))
            if (i + 1, j) in symbol_locations:
                gear_list.add((i + 1, j))
            if (i - 1, j) in symbol_locations:
                gear_list.add((i - 1, j))
            if (i + 1, j + 1) in symbol_locations:
                gear_list.add((i + 1, j + 1))
            if (i + 1, j - 1) in symbol_locations:
                gear_list.add((i + 1, j - 1))
            if (i - 1, j - 1) in symbol_locations:
                gear_list.add((i - 1, j - 1))
            if (i - 1, j + 1) in symbol_locations:
                gear_list.add((i - 1, j + 1))
                
        
        #we have reached the end of a number
        if numFound and ((not lines[i][j].isdigit()) or j == len(lines[0]) - 2):
            #for each element in the set, add to the dictionary
            for gear in gear_list:
                if not gear in gear_dict:
                    gear_dict[gear] = []
                gear_dict[gear].append(int(cur_num))
     
            numFound = False
            cur_num = ''
            gear_list = set()
        

for key in gear_dict:
    if len(gear_dict[key]) == 2:
        gear_ratio = gear_dict[key][0] * gear_dict[key][1]
        total += gear_ratio

print(total)