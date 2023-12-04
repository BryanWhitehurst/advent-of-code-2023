f = open("input.txt", "r")

lines = f.readlines()

total = 0
for line in lines: 
    cur_winning_nums, cur_my_nums = line.split(" | ")
    cur_winning_nums = cur_winning_nums.split(": ")[1].strip()
    cur_winning_nums = cur_winning_nums.split()
    cur_my_nums = cur_my_nums.split()
    cur_total = 0 
    for num in cur_my_nums:
        if num in cur_winning_nums:
            if cur_total == 0: cur_total = 1
            else: cur_total *= 2 

    total += cur_total

print(total) 
