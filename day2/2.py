f = open("input.txt", "r")

lines = f.readlines()

total = 0

for line in lines:
    game_id, rounds = line.split(":")
    game_id = int(game_id.split()[1])

    max_red = 0
    max_green = 0 
    max_blue = 0

    rounds = rounds.split(";")
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
        
        max_red  = int(num_red) if int(num_red) > max_red else max_red
        max_blue  = int(num_blue) if int(num_blue) > max_blue else max_blue
        max_green  = int(num_green) if int(num_green) > max_green else max_green
    
    total += max_red * max_blue * max_green

print(total)

