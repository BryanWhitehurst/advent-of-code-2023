f = open("input.txt", "r")
#read input into 2d array
lines = f.readlines()

#find the index of 'S'
starting_position = ()
for i in range(len(lines)):
    j = lines[i].find('S')
    if j == -1: continue

    starting_position = (i, j)
    break

#navigate through the pipe, keeping track of the total length of the pipe
cur_type = 'S'
prev_pos = starting_position
cur_pos = starting_position
start = True
loop_positions = [starting_position]

#break loop whenever S is found
while(True):
    if (not start) and lines[cur_pos[0]][cur_pos[1]] == 'S':
        break
    if start: start = False
    
     #check above cur_pos
    if cur_type == '|' or cur_type == 'J' or cur_type == 'L' or cur_type == 'S':
        if cur_pos[0] != 0 and prev_pos != (cur_pos[0] - 2, cur_pos[1]) and lines[cur_pos[0] - 1][cur_pos[1]] == '|':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0] - 1, cur_pos[1]))
            cur_pos = (cur_pos[0] - 2, cur_pos[1])
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != 0 and prev_pos != (cur_pos[0] - 1, cur_pos[1] - 1) and lines[cur_pos[0] - 1][cur_pos[1]] == '7':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0] - 1, cur_pos[1]))
            cur_pos = (cur_pos[0] - 1, cur_pos[1] - 1)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != 0 and prev_pos != (cur_pos[0] - 1, cur_pos[1] + 1) and lines[cur_pos[0] - 1][cur_pos[1]] == 'F':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0] - 1, cur_pos[1]))
            cur_pos = (cur_pos[0] - 1, cur_pos[1] + 1)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

    #below cur_pos
    if cur_type == '|' or cur_type == '7' or cur_type == 'F' or cur_type == 'S':
        if cur_pos[0] != (len(lines) - 1) and prev_pos != (cur_pos[0] + 2, cur_pos[1]) and lines[cur_pos[0] + 1][cur_pos[1]] == '|':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0] + 1, cur_pos[1]))
            cur_pos = (cur_pos[0] + 2, cur_pos[1])
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != (len(lines) - 1) and prev_pos != (cur_pos[0] + 1, cur_pos[1] + 1)  and lines[cur_pos[0] + 1][cur_pos[1]] == 'L':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0] + 1, cur_pos[1]))
            cur_pos = (cur_pos[0] + 1, cur_pos[1] + 1) 
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != (len(lines) - 1) and prev_pos != (cur_pos[0] + 1, cur_pos[1] - 1) and lines[cur_pos[0] + 1][cur_pos[1]] == 'J':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0] + 1, cur_pos[1]))
            cur_pos = (cur_pos[0] + 1, cur_pos[1] - 1) 
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

    #left of cur_pos
    if cur_type == '-' or cur_type == '7' or cur_type == 'J' or cur_type == 'S':
        if cur_pos[1] != 0 and prev_pos != (cur_pos[0], cur_pos[1] - 2) and lines[cur_pos[0]][cur_pos[1] - 1] == '-':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0], cur_pos[1] - 1))
            cur_pos = (cur_pos[0], cur_pos[1] - 2)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != 0 and prev_pos != (cur_pos[0] - 1, cur_pos[1] - 1) and lines[cur_pos[0]][cur_pos[1] - 1] == 'L':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0], cur_pos[1] - 1))
            cur_pos = (cur_pos[0] - 1, cur_pos[1] - 1)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != 0 and prev_pos != (cur_pos[0] + 1, cur_pos[1] - 1) and lines[cur_pos[0]][cur_pos[1] - 1] == 'F':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0], cur_pos[1] - 1))
            cur_pos = (cur_pos[0] + 1, cur_pos[1] - 1)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

    #right of cur_pos

    if cur_type == '-' or cur_type == 'F' or cur_type == 'L' or cur_type == 'S':
        if cur_pos[1] != (len(lines[0]) - 1) and prev_pos != (cur_pos[0], cur_pos[1] + 2) and lines[cur_pos[0]][cur_pos[1] + 1] == '-':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0], cur_pos[1] + 1))
            cur_pos = (cur_pos[0], cur_pos[1] + 2)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != (len(lines[0]) - 1) and prev_pos != (cur_pos[0] - 1, cur_pos[1] + 1) and lines[cur_pos[0]][cur_pos[1] + 1] == 'J':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0], cur_pos[1] + 1))
            cur_pos = (cur_pos[0] - 1, cur_pos[1] + 1)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != (len(lines[0]) - 1) and prev_pos != (cur_pos[0] + 1, cur_pos[1] + 1) and lines[cur_pos[0]][cur_pos[1] + 1] == '7':
            prev_pos = cur_pos
            loop_positions.append((cur_pos[0], cur_pos[1] + 1))
            cur_pos = (cur_pos[0] + 1, cur_pos[1] + 1)
            loop_positions.append(cur_pos)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

#replace all pipe pieces that aren't apart of the loop with dots to make next part easier
for i in range(len(lines)):
     for j in range(len(lines[0]) - 1):
         if (i, j) not in loop_positions:
            string_list = list(lines[i])
            string_list[j] = '.'
            lines[i] = "".join(string_list)

total = 0
for i in range(len(lines)):
    cur_count  = 0
    wall_found = False
    lFound = False
    fFound = False
    for j in range(len(lines[0]) - 1):
        
        if lines[i][j] == '|' or lines[i][j] == 'S':
            wall_found = not wall_found

        elif lFound and lines[i][j] == '7':
            wall_found = not wall_found
            lFound = False

        elif lFound and lines[i][j] == 'J':
            lFound = False

        elif fFound and lines[i][j] == 'J':
            wall_found = not wall_found
            fFound = False

        elif fFound and lines[i][j] == '7':
            fFound = False
        
        elif lFound and lines[i][j] == '-':
            continue

        elif lines[i][j] == 'L':
            lFound = True

        elif lines[i][j] == 'F':
            fFound = True

        elif wall_found and lines[i][j] == '.':
            cur_count += 1


    total += cur_count
print(total)