f = open("input.txt", "r")

lines = f.readlines()
sequences = []
for line in lines:
    sequences.append(list(map(lambda x: int(x), line.strip().split())))

def getNextSequenceValue(seq):
    global_differences = [seq.copy()]
    numsDifferent = False
    cur_differences = global_differences[0]
    while(True):
        new_differences = []
        numsDifferent = False
        for i in range(len(cur_differences) - 1):
            diff = cur_differences[i + 1] - cur_differences[i]
            if i > 1 and diff != new_differences[-1]:
                numsDifferent = True

            new_differences.append(diff)
        
        global_differences.append(new_differences)
        #break, start working backwards
        if not numsDifferent:
            break

        else:
            #check for differences in new array
            cur_differences = new_differences

    #pop the last array, subtract the last element from the first element
    while(len(global_differences) != 1):
        last_array = global_differences.pop()
        global_differences[-1][0] -= last_array[0]

    return global_differences[0][0]

total = 0
for seq in sequences:
    total += getNextSequenceValue(seq)

print(total)