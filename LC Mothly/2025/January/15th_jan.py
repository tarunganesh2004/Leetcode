# Minimize XOR, LC 2429

# Given two positive integers num1 and num2, find the positive integer x such that:

# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# return x

num1=3
num2=5
# def minimizeXORBrute(num1,num2): # This takes lots of time and is worst approach
#     c2=num2.bit_count() # count of set bits in num2
#     min_x=None
#     min_xor=float('inf')
#     for x in range(0,1<<32):
#         if x.bit_count()==c2:
#             xor=x^num1
#             if xor<min_xor:
#                 min_xor=xor
#                 min_x=x
#     return min_x

# optimal approach is to find the number of set bits in num2 and then set the same number of set bits in x
def minimizeXOR(num1,num2): # Optimized O(32) & O(1)
    c2=num2.bit_count()
    x=0
    for i in range(31,-1,-1):
        if c2==0:
            break
        if num1 &(1<<i): # if ith bit is set in num1
            x|=(1<<i) # set the ith bit in x
            c2-=1
    for i in range(32): # if still c2 is not 0 then set the remaining bits

        if c2==0:
            break
        if not num1 &(1<<i): # if ith bit is not set in num1
            x|=(1<<i) 
            c2-=1
    return x

print(minimizeXOR(num1,num2)) # 3