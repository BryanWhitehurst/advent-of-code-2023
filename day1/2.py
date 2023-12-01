f = open("input.txt", "r")

lines = f.readlines()

def convert_num(str):
    if str == 'one':
        return '1'
    elif str == 'two':
        return '2'
    elif str == 'three':
        return '3'
    elif str == 'four':
        return '4'
    elif str == 'five':
        return '5'
    elif str == 'six':
        return '6'
    elif str == 'seven':
        return '7'
    elif str == 'eight':
        return '8'
    elif str == 'nine':
        return '9'

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0
for line in lines: 
    smallest = [10, 500]
    largest = [10, -1]
    print(line)
    for num in numbers:
        index = list(find_all(line, num))
        if len(index) != 0:
            first = index[0]
            if len(index) == 1: 
                last = first
            else: last = index[-1]

            if first < smallest[1]:
                smallest = [num, first]
            
            if last > largest[1]:
                largest = [num, last]

    val1 = smallest[0]
    if val1.isalpha():
        val1 = convert_num(val1)

    val2 = largest[0]
    if val2.isalpha():
        val2 = convert_num(val2)

    total += int(val1 + val2)

print(total)