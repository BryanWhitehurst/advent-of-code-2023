f = open("input.txt", "r")

lines = f.readlines()

times = lines[0].split("Time:      ")[1].split()
times = list(map(lambda x: int(x.strip()), times))
records = lines[1].split("Distance:  ")[1].split()
records = list(map(lambda x: int(x.strip()), records))

totals = []
for i in range(len(times)):
    num_ways_to_beat = 0
    #time remaining * amount of time to hold button = distance traveled
    for j in range(times[i]):
        #j = amount of time to hold the button
        #time remaining = times[i] - j
        distance = j * (times[i] - j)
        if distance > records[i]:
            num_ways_to_beat += 1
    totals.append(num_ways_to_beat)

print(totals)
print(totals[0] * totals[1] * totals[2] * totals[3])