f = open("input.txt", "r")

lines = f.readlines()

total = 0
for line in lines:
    game_id, rounds = line.split(":")
    game_id = int(game_id.split()[1])
    
    rounds = rounds.split(";")
    possible = True
    for round in rounds:
        num_red = 0
        num_blue = 0
        num_green = 0
        if round.find(",") != -1:
            colors = round.split(",")
            
            for color in colors:
                if color.find("red") != -1:
                    num_red = color.strip().split()[0]
                elif color.find("blue") != -1:
                    num_blue = color.strip().split()[0] 
                elif color.find("green") != -1:
                    num_green = color.strip().split()[0]
        else:
            if round.find("red") != -1:
                num_red = round.strip().split()[0]
            elif round.find("blue") != -1:
                num_blue = round.strip().split()[0]  
            elif round.find("green") != -1:
                num_green = round.strip().split()[0]

        if(int(num_red) > 12 or int(num_blue) > 14 or int(num_green) > 13):
            possible = False
            break
    
    if possible:
        total += game_id

print(total)

