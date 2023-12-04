f = open("input.txt", "r")

lines = f.readlines()
symbol_locations = []
total = 0

#get indicies of symbols, get indicies of numbers 
#compare indicies to determine if part needs to be added
for i in range(len(lines)):
    for j in range(len(lines[0]) -1):
        #if symbol found, append to symbol list
        if (not lines[i][j].isdigit()) and (not lines[i][j] == '.'):
            symbol_locations.append((i, j))

for i in range(len(lines)):
    cur_num = ''
    numFound = False
    symbolAdjacent = False
    for j in range(len(lines[0]) - 1):
        if lines[i][j].isdigit():
            cur_num += lines[i][j]
            numFound = True

            #check if adjacent to symbol
            if ((i, j + 1) in symbol_locations or
                (i, j - 1) in symbol_locations or
                (i + 1, j) in symbol_locations or
                (i - 1, j) in symbol_locations or
                (i + 1, j + 1) in symbol_locations or
                (i + 1, j - 1) in symbol_locations or
                (i - 1, j - 1) in symbol_locations or
                (i - 1, j + 1) in symbol_locations):
                symbolAdjacent = True
        
        #we have reached the end of a number
        if numFound and ((not lines[i][j].isdigit()) or j == len(lines[0]) - 2):
            if symbolAdjacent:
                total += int(cur_num)
            
            numFound = False
            symbolAdjacent = False
            cur_num = ''
        
print(total)
        