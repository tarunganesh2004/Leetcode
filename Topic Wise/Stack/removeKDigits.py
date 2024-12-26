# Remove K digits

num="1432219"
num1="10"
k=3
k1=1

def removeKDigits(nums,k):
    if len(nums)<=k:
        return "0"
    
    stack=[]
    for i in range(len(nums)):
        while stack and stack[-1]>nums[i] and k:
            stack.pop()
            k-=1
        stack.append(nums[i])
    
    # if there are still k elements to be removed
    while k:
        stack.pop()
        k-=1
    
    # remove the leading zeroes
    res="".join(stack).lstrip("0")
    
    return res if res else "0"

print(removeKDigits(num,k)) # 1219
print(removeKDigits(num1,k1)) # 0