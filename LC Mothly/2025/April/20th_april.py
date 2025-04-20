# Rabbits in Forest LC 781

answers=[1,1,2]

def numRabbits(answers):
    counts={}
    count=0

    for ans in answers:
        if ans==0:
            # only rabit of its color 
            count+=1
        elif ans not in counts or counts[ans]==0:
            # this is the fitst time the color appears
            counts[ans]=1

            # add all rabbits having this new color
            count+= ans+1
        else:
            # this color has already appeared
            counts[ans]-=1
            if counts[ans]>ans:
                # the group is complete
                counts[ans]=0
        
    return count

print(numRabbits(answers)) # Output: 5