# Check if Array is Sorted and Rotated LC 1752

nums=[3,4,5,1,2]

def check(nums):
    n=len(nums)
    sorted_nums=sorted(nums)
    for i in range(n):
        is_match=True
        for j in range(n):
            if nums[(i+j)%n]!=sorted_nums[j]:
                is_match=False
                break
        if is_match:
            return True
        
    return False

print(check(nums))