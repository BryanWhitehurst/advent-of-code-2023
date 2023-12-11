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
pipe_count = 0
#break loop whenever S is found
while(True):
    if (not start) and lines[cur_pos[0]][cur_pos[1]] == 'S':
        break
    if start: start = False
    
    pipe_count += 2

     #check above cur_pos
    if cur_type == '|' or cur_type == 'J' or cur_type == 'L' or cur_type == 'S':
        if cur_pos[0] != 0 and prev_pos != (cur_pos[0] - 2, cur_pos[1]) and lines[cur_pos[0] - 1][cur_pos[1]] == '|':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] - 2, cur_pos[1])
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != 0 and prev_pos != (cur_pos[0] - 1, cur_pos[1] - 1) and lines[cur_pos[0] - 1][cur_pos[1]] == '7':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] - 1, cur_pos[1] - 1)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != 0 and prev_pos != (cur_pos[0] - 1, cur_pos[1] + 1) and lines[cur_pos[0] - 1][cur_pos[1]] == 'F':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] - 1, cur_pos[1] + 1)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

    #below cur_pos
    if cur_type == '|' or cur_type == '7' or cur_type == 'F' or cur_type == 'S':
        if cur_pos[0] != (len(lines) - 1) and prev_pos != (cur_pos[0] + 2, cur_pos[1]) and lines[cur_pos[0] + 1][cur_pos[1]] == '|':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] + 2, cur_pos[1])
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != (len(lines) - 1) and prev_pos != (cur_pos[0] + 1, cur_pos[1] + 1)  and lines[cur_pos[0] + 1][cur_pos[1]] == 'L':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] + 1, cur_pos[1] + 1) 
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[0] != (len(lines) - 1) and prev_pos != (cur_pos[0] + 1, cur_pos[1] - 1) and lines[cur_pos[0] + 1][cur_pos[1]] == 'J':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] + 1, cur_pos[1] - 1) 
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

    #left of cur_pos
    if cur_type == '-' or cur_type == '7' or cur_type == 'J' or cur_type == 'S':
        if cur_pos[1] != 0 and prev_pos != (cur_pos[0], cur_pos[1] - 2) and lines[cur_pos[0]][cur_pos[1] - 1] == '-':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0], cur_pos[1] - 2)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != 0 and prev_pos != (cur_pos[0] - 1, cur_pos[1] - 1) and lines[cur_pos[0]][cur_pos[1] - 1] == 'L':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] - 1, cur_pos[1] - 1)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != 0 and prev_pos != (cur_pos[0] + 1, cur_pos[1] - 1) and lines[cur_pos[0]][cur_pos[1] - 1] == 'F':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] + 1, cur_pos[1] - 1)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue

    #right of cur_pos

    if cur_type == '-' or cur_type == 'F' or cur_type == 'L' or cur_type == 'S':
        if cur_pos[1] != (len(lines[0]) - 1) and prev_pos != (cur_pos[0], cur_pos[1] + 2) and lines[cur_pos[0]][cur_pos[1] + 1] == '-':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0], cur_pos[1] + 2)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != (len(lines[0]) - 1) and prev_pos != (cur_pos[0] - 1, cur_pos[1] + 1) and lines[cur_pos[0]][cur_pos[1] + 1] == 'J':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] - 1, cur_pos[1] + 1)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
        elif cur_pos[1] != (len(lines[0]) - 1) and prev_pos != (cur_pos[0] + 1, cur_pos[1] + 1) and lines[cur_pos[0]][cur_pos[1] + 1] == '7':
            prev_pos = cur_pos
            cur_pos = (cur_pos[0] + 1, cur_pos[1] + 1)
            cur_type = lines[cur_pos[0]][cur_pos[1]]
            continue
    
print(int(pipe_count/2))
