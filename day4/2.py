f = open("input.txt", "r")

lines = f.readlines()

winning_nums = []
my_nums = []
total = 0
for line in lines: 
    cur_winning_nums, cur_my_nums = line.split(" | ")
    cur_winning_nums = cur_winning_nums.split(": ")[1].strip()
    cur_winning_nums = cur_winning_nums.split()
    cur_my_nums = cur_my_nums.split()
    winning_nums.append(cur_winning_nums)
    my_nums.append(cur_my_nums)

#gets all of the recursive cards
def process_card(cur_index):
    cur_my_nums = my_nums[cur_index]
    cur_winning_nums = winning_nums[cur_index]
    recursive_index = cur_index
    global total
    for num in cur_my_nums:
        if num in cur_winning_nums:
            total += 1
            recursive_index += 1
          
            #if we are on the last card, don't make any more recursive calls
            if not recursive_index == len(my_nums):
                process_card(recursive_index)

total = len(my_nums)
for i in range(len(my_nums)): process_card(i)

print(total) 
