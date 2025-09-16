# Replace Non Coprime Numbers in Array LC 2197(Hard)

nums=[6,4,3,2,7,6,2]

def replaceNonCoprime(nums):
    from math import gcd,lcm
    stack = []
    for n in nums:
        stack.append(n)
        while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
            stack.append(lcm(stack.pop(), stack.pop()))
    return stack

print(replaceNonCoprime(nums))