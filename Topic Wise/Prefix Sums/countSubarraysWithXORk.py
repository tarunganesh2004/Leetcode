# Count subarrays with xor k

arr = [4, 2, 2, 6, 4]


# bruteforce O(n^2)
def bruteForce(arr, k):
    c = 0
    for i in range(len(arr)):
        xor = 0
        for j in range(i, len(arr)):
            xor ^= arr[j]
            if xor == k:
                c += 1
    return c


# using map,prefix xor
def countSubarrays(arr, k):
    map = {0: 1}  # to handle subarrays starting from 0th index, index:xor value
    cur_xor = 0
    count = 0
    for num in arr:
        cur_xor ^= num
        target = cur_xor ^ k
        if target in map:
            count += map[target]
        # if cur_xor is already in map, then increment its value by 1
        map[cur_xor] = map.get(cur_xor, 0) + 1

    return count

def printSubarrayswithxork(arr,k):
    prefix_map={0:[-1]} # store indices where prefix_xor is found
    cur_xor=0
    count=0
    for i,num in enumerate(arr):
        cur_xor^=num
        target=cur_xor^k
        if target in prefix_map:
            count+=len(prefix_map[target]) # add the number of indices where target is found
            for start_index in prefix_map[target]:
                print(arr[start_index+1:i+1])

        if cur_xor in prefix_map:
            prefix_map[cur_xor].append(i)
        else:
            prefix_map[cur_xor]=[i]
    
    return count


print(bruteForce(arr, 6))
print(countSubarrays(arr, 6))

print(printSubarrayswithxork(arr,6))