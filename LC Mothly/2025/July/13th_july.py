# Maximum Matching of Players with Trainers LC 2410

players=[4,7,9]
trainers=[8,2,5,8]

def matchPlayersAndTrainers(players,trainers):
    players.sort()
    trainers.sort()
    count=0
    i=j=0
    while i < len(players) and j < len(trainers):
        if players[i] <= trainers[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

print(matchPlayersAndTrainers(players, trainers))  