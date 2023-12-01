f = open("input.txt", "r")

lines = f.readlines()

total = 0
for l in lines:
    num_list = []
    for letter in l:
        if letter.isnumeric() and len(num_list) != 2:
            num_list.append(letter)
        elif letter.isnumeric():
           num_list[1] = letter
    
    if len(num_list) == 1:
        num_list.append(num_list[0])
        
    total += int(num_list[0] + num_list[1])
print(total)       
