# Total Characters in String After Transformations II LC 3337

s="abcyy"
t=2
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]


def lengthAfterTransformations(s, t,nums):
    mod=10**9 + 7
    def mat_mult(A, B):
        n=len(A)
        C=[[0]*n for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if A[i][k]:
                    a=A[i][k]
                    for j in range(n):
                        C[i][j]=(C[i][j]+a*B[k][j])%mod
        return C
    
    def mat_pow(A, p):
        n=len(A)
        res=[[0]*n for _ in range(n)]
        for i in range(n):
            res[i][i]=1
        while p:
            if p%2:
                res=mat_mult(res, A)
            A=mat_mult(A, A)
            p//=2
        return res
    
    n=26
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(1,nums[i]+1):
            j=(i+k)%n
            A[i][j]=1

    if t==0:
        return len(s)%mod
    
    M=mat_pow(A, t)
    res=0
    for ch in s:
        res=(res+sum(M[ord(ch)-ord('a')]))%mod
    return res

print(lengthAfterTransformations(s, t, nums))