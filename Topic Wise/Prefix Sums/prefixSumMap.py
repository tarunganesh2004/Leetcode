arr=[1,2,-1,2,-2,3]
def prefixsumMap(arr):
    """
    Computes prefix sums and stores them in a map.
    The map stores:
    - Key: The prefix sum value.
    - Value: Frequency of that prefix sum value.
    """

    prefixSum=0
    map={}
    
    for i in range(len(arr)):
        prefixSum+=arr[i]

        if prefixSum in map:
            map[prefixSum]+=1
        else:
            map[prefixSum]=1
    
    return map

print(prefixsumMap(arr)) # {1: 1, 3: 1, 2: 1, 4: 1, 2: 1, 5: 1, 3: 1, 6: 1, 4: 1, 7: 1}