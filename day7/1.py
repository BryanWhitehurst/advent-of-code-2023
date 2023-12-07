f = open("input.txt", "r")

def getHandType(hand):
    card_types ={'A' : 0, 'K' : 0, 'Q' : 0, 'J' : 0, 'T' : 0, '9': 0, '8' : 0, '7' : 0, '6' : 0, '5' : 0, '4' : 0, '3' : 0, '2' : 0}
    #get count of every possible card type
    for char in hand:
        card_types[char] += 1
    
    card_types_copy = card_types.copy()
    for key in card_types_copy.keys():
        if card_types[key] == 0:
            del card_types[key]
    
    values = list(card_types.values())
    values.sort(reverse=True)

    if len(card_types) == 1:
        return 6 #five of a kind
    
    elif len(card_types) == 2 and values[0] == 4:
        return 5 #four of a kind
    
    elif len(card_types) == 2 and values[0] == 3:
        return 4 #full house

    elif len(card_types) == 3 and values[0] == 3:
        return 3 #Three of a kind
    
    elif len(card_types) == 3 and values[0] == 2:
        return 2 #Two Pair
    
    elif len(card_types) == 4:
        return 1 #One Pair
    
    elif len(card_types) == 5:
        return 0 #High Card
    
#should return the hand with the lowest rank
def tieBreak(hands):
    card_types = 'AKQJT98765432'
    cur_winner = hands[0]
    for i in range(1, len(hands)):
        next_hand = hands[i]

        for j in range(len(next_hand)):
            #next hand has a lower rank, return it
            if card_types.find(cur_winner[0][j]) <  card_types.find(next_hand[0][j]):
                cur_winner = next_hand
                break
            
            if card_types.find(cur_winner[0][j]) >  card_types.find(next_hand[0][j]):
                break
    return cur_winner

lines = f.readlines()
ranks = [[], [], [], [], [], [], []]
for line in lines:
    hand, bid = line.split()
    rank = getHandType(hand)
    ranks[rank].append([hand, int(bid)])

while [] in ranks:
    ranks.remove([])

final_rankings = []
for rank in ranks:
    if len(rank) > 1:
        
        while(len(rank) != 1):
            lowest_rank = tieBreak(rank)
            rank.remove(lowest_rank)
            final_rankings.append(lowest_rank)
        
        #with one hand left, append it to the end of the list
        final_rankings.append(rank[0])

    else:
        final_rankings.append(rank[0])

total = 0
for i in range(len(final_rankings)):
    total += final_rankings[i][1] * (i + 1)

print(total)
