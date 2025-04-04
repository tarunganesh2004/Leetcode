# Maximum Value of an Ordered Triplet II LC 2874

nums=[12,6,1,2,7]

# optimized
def maximumTripletValue(nums):
    maxTriplet,maxElement,maxDiff=0,0,0
    for num in nums:
        maxTriplet=max(maxTriplet,maxDiff*num)
        maxDiff=max(maxDiff,maxElement-num)
        maxElement=max(maxElement,num)
    return maxTriplet

print(maximumTripletValue(nums))