# Minimum Operations to Make the Integer Zero LC 2749

num1=3
num2=-2

def minOperations(num1,num2):
    for k in range(1,61):
        # here k is the number of operations
        # x is sum of powers of 2 
        x=num1-k*num2 
        # print(x)
        if x>=0:
            bits=bin(x).count('1') # bitcount of x
            # we need atleast 'bits ' operations(one for each set bit)
            # and atmost 'x' operations (if we split everything into 1's
            # so k must lie between bits and x
            if bits<=k<=x:
                return k 
    return -1

print(minOperations(num1,num2))