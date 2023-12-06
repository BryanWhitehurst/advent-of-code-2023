import sys
f = open("input.txt", "r")

lines = f.readlines()

seeds = lines[0].split(': ')[1].strip().split()
seeds = list(map(lambda x: int(x), seeds))

list_of_maps = []
cur_rows = []
i = 3
while i < len(lines): 
    if lines[i] == '\n':
        list_of_maps.append(cur_rows)
        cur_rows = []
        i += 2
        continue
    
    cur_rows.append(list(map(lambda x: int(x), lines[i].strip().split())))
    i += 1

    if i == len(lines):
        list_of_maps.append(cur_rows)


final_val = sys.maxsize

seed_dict = {}
i = 0
while i < len(seeds):
    seed_dict[seeds[i]] = seeds[i] + seeds[i + 1] - 1
    i += 2

def transform_seeds(mapping2, seed_dict_orig):
    seed_dict = seed_dict_orig.copy()
    transform = {}
    for mapping in mapping2:
        for seed_start in seed_dict_orig:
            seed_end = seed_dict[seed_start]

            src_start = mapping[1]
            src_end = mapping[1] + mapping[2] - 1

            dest_start = mapping[0]
            dest_end = mapping[0] + mapping[2] - 1

            #enclosed
            if seed_start >= src_start and seed_end <= src_end:
                del seed_dict[seed_start]
                transform[dest_start + (seed_start - src_start)] = dest_start + (seed_end - src_start)
            
            #overlap on right
            elif seed_start >= src_start and seed_start <= src_end and seed_end > src_end:
                del seed_dict[seed_start]
                transform[dest_start + (seed_start - src_start)] = dest_end
                transform[src_end + 1] = seed_end

            #overlap on left
            elif seed_start < src_start and seed_end >= src_start and seed_end <= src_end:
                transform[seed_start] = src_start - 1
                transform[dest_start] = dest_start + seed_end - src_start
            
            #completely encloses map range
            elif seed_start < src_start and seed_end > src_end:
                transform[seed_start] = src_start - 1
                transform[src_end + 1] = seed_end
                transform[dest_start] = dest_end
            
            #if no overlap at all, do nothing
        seed_dict_orig = seed_dict.copy()

    #add new keys back to seed_dict before returning
    for key in transform:
        seed_dict[key] = transform[key]
    return seed_dict

for mapping in list_of_maps:
    seed_dict = transform_seeds(mapping, seed_dict)

print(min(list(seed_dict.keys())))