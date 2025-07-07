# Find Lucky Integer in an Array LC 1394

arr=[2,2,3,4]

def findLucky(arr):
    count={}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    lucky = -1
    for num, freq in count.items():
        if num == freq:
            lucky = max(lucky, num)
            
    return lucky

print(findLucky(arr))  # Output: 2