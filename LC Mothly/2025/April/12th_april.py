# # Find the count of Good Integers LC 3272(Hard)

# You are given two positive integers n and k.

# An integer x is called k-palindromic if:

# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

# Return the count of good integers containing n digits.

# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

from collections import Counter


n=3
k=5

def countGoodIntegers(n,k):
    if n==1:
        total=0
        for i in range(1,10):
            if i%k==0:
                total+=1
        return total
    
    fact=[1]
    for i in range(1,n+1):
        fact.append(fact[-1]*i)

    seen=set()
    ans=0
    for left in range(10**((n-1)//2),10**((n+1)//2)):
        l=str(left)  # noqa: E741
        r=l[::-1]
        if n%2==1:
            r=r[1:]
        t=l+r

        if int(t)%k!=0:
            continue

        s="".join(sorted(list(t)))
        if s in seen:
            continue
        seen.add(s)
        count=Counter(t)

        total=fact[n]
        for key in count.keys():
            total//=fact[count[key]]
        ans+=total

        if count["0"]>=1:
            total_non_zero=fact[n-1]
            count["0"]-=1

            for key in count.keys():
                total_non_zero//=fact[count[key]]
            ans-=total_non_zero

    return ans


print(countGoodIntegers(n, k))