# Maximize Subarrays After Removing One Conflicting Pair LC 3480(Hard)

n=4
conflictingPairs=[[2,3],[1,4]]

def maxSubarrays(n, conflictingPairs):
    right=[[] for _ in range(n+1)]
    for a,b in conflictingPairs:
        right[max(a,b)].append(min(a,b))
    ans=0

    left=[0,0]
    imp=[0]*(n+1)
    for r in range(1,n+1):
        for l in right[r]:  # noqa: E741
            left=max(left,[l,left[0]],[left[0],l])
        ans+=r-left[0]
        imp[left[0]]+=left[0]-left[1]

    return ans+max(imp)

print(maxSubarrays(n, conflictingPairs))  # Output: 9
