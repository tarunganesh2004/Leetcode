# Number of Equivalent Domino Pairs LC 1128

dominoes= [[1,2],[2,1],[3,4],[5,6]]

def numEquivDominoPairs(dominoes):
    count= {}
    for a, b in dominoes:
        key= (min(a, b), max(a, b))
        count[key]= count.get(key, 0) + 1
    result= 0
    for value in count.values():
        result += value * (value - 1) // 2
    return result

print(numEquivDominoPairs(dominoes))  # Output: 1