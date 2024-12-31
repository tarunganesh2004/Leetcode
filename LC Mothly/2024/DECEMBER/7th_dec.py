# Minimum Limit of Balls in a Bag LC 1760

nums=[9]
maxOperations=2

def minimumSize(nums,maxOperations):
    l=1  # noqa: E741
    r=max(nums)
    while l<r:
        m=(l+r)//2
        if sum((x-1)//m for x in nums)>maxOperations:
            l=m+1
        else:
            r=m
    return l

print(minimumSize(nums,maxOperations))