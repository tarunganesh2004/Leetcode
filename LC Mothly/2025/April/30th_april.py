# Find Numbers with Even Number of Digits LC 1295

nums=[12,345,2,6,7896]

def findNumbers(nums):
    c=0
    for num in nums:
        if len(str(num))%2==0:
            c+=1
    return c

print(findNumbers(nums)) # Output: 2