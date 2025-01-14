# # Find the prefix common array of two arrays LC 2657

# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

A=[1,3,2,4]
B=[3,1,2,4] # o/p : at i=0 no number is common so c[0]=0,
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
# o/p: [0,2,3,4]

def findthePrefixCommonArray(A,B): # O(n) & O(n)
    n=len(A)
    C=[0]*n
    seta,setb=set(),set()
    for i in range(n):
        # to get the previous count
        C[i]=C[i-1] 

        # if both are same then increment the count
        if A[i]==B[i]:
            C[i]+=1
        else:
            # if already A[i] is present in setb , then its a common number increment
            if A[i] in setb:
                C[i]+=1
            # if already B[i] is present in seta , then its a common number increment
            if B[i] in seta:
                C[i]+=1
            seta.add(A[i])
            setb.add(B[i])
    return C

def anotherApproach(A,B):
    # using set intersection
    n = len(A)
    common = [0] * n
    for i in range(n):
        common[i] = len(set(A[: i + 1]).intersection(set(B[: i + 1])))
    return common

print(findthePrefixCommonArray(A,B)) # [0,2,3,4]
