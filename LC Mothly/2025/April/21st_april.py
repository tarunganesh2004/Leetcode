# Count the Hidden Sequences LC 2145

differences=[1,-3,4]
lower=1
upper=6

# two possible sequences are
# [3,4,1,5]
# [4,5,2,6]

# idea is to use prefix sum to find the min and max of the sequence

def numberOfArrays(differences,lower,upper):
    prefix=[0]
    for d in differences:
        prefix.append(prefix[-1]+d)

    min_a0=max(lower-x for x in prefix)
    max_a0=min(upper-x for x in prefix)
    return max(0,max_a0-min_a0+1)

print(numberOfArrays(differences,lower,upper)) # Output: 2