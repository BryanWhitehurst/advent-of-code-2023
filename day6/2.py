f = open("input.txt", "r")

lines = f.readlines()

times = lines[0].split("Time:      ")[1].split()
times = list(map(lambda x: x.strip(), times))
records = lines[1].split("Distance:  ")[1].split()
records = list(map(lambda x: x.strip(), records))

times = times[0] + times[1] + times[2] + times[3]
records = records[0] + records[1] + records[2] + records[3]


num_ways_to_beat = 0
#time remaining * amount of time to hold button = distance traveled
for j in range(int(times)):
    #j = amount of time to hold the button
    #time remaining = times[i] - j
    distance = j * (int(times) - j)
    if distance > int(records):
        num_ways_to_beat += 1

print(num_ways_to_beat)