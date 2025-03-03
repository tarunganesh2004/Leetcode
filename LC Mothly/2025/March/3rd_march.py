# Partition Array According to given pivot LC 2161

nums=[9,12,5,10,14,3,10]
pivot=10

def pivotArray(nums,pivot):
    less,equal,more=[],[],[]

    for i in nums:
        if i<pivot:
            less.append(i)
        elif i==pivot:
            equal.append(i)
        else:
            more.append(i)
    return less+equal+more

print(pivotArray(nums,pivot))