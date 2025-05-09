# Count Number of Balanced Permutations LC 3343

from collections import Counter
from functools import lru_cache
from math import comb

num="123"

def countBalancedPermutationsBrute(num): # TLE. 
    # TC O(n! * n) where n is the length of num.
    # find permutations of number
    from itertools import permutations
    perms = set(permutations(num)) # get unique permutations
    count=0

    def isBalanced(p):
        # check if the permutation is balanced
        n=len(p)
        leftSum=0
        rightSum=0

        for i in range(n):
            if i<n//2:
                leftSum+=int(p[i])
            else:
                rightSum+=int(p[i])

        return leftSum==rightSum
    
    for p in perms:
        if isBalanced(p):
            count+=1

    return count

# optimal solution
def countBalancedPermutationsOptimal(num):
    MOD=10**9+7
    cnt=Counter(int(ch) for ch in num)
    total=sum(int(ch) for ch in num)

    if total%2!=0:
        return 0
    
    half_sum=total//2
    n=len(num)
    even_count=n//2
    odd_count=n-even_count
    @lru_cache(maxsize=None)
    def dfs(digit,odd,even,balance):
        if odd==0 and even==0 and balance==0:
            return 1
        if digit<0 or odd<0 or even<0 or balance<0:
            return 0
        
        res=0
        for j in range(0,cnt[digit]+1):
            odd_used=j
            even_used=cnt[digit]-j
            if odd_used>odd or even_used>even:
                continue
            comb_odd=comb(odd,odd_used)
            comb_even=comb(even,even_used)
            res+=comb_odd*comb_even*dfs(
                digit-1,
                odd-odd_used,
                even-even_used,
                balance-digit*odd_used
            )
            res%=MOD
        return res
    
    return dfs(9,odd_count,even_count,half_sum)




print(countBalancedPermutationsBrute(num))  
print(countBalancedPermutationsOptimal(num))  