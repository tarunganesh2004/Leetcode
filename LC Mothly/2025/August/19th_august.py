# Number of Zero Filled Subarrays LC 2348

nums= [1, 3, 0, 0, 2, 0, 0, 4]

def zeroFilledSubarray(nums):
    count = 0
    total = 0
    
    for num in nums:
        if num == 0:
            count += 1
            print(f"Found zero, current count: {count}")
            total += count
            print(f"Current total: {total}")
        else:
            count = 0
            
    return total

print(zeroFilledSubarray(nums)) 