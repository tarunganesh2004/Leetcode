# # Total Characters in String After Transformations I LC 3335

# # You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.

s="abcyy"
t=2

def lengthAfterTransformationsBrute(s, t):
    mod=10**9 + 7
    for _ in range(t):
        new_s = []
        for char in s:
            if char == 'z':
                new_s.append('ab')
            else:
                new_s.append(chr(ord(char) + 1))
        s = ''.join(new_s)
    return len(s)%mod

# optimized 
def lengthAfterTransformationsOptimized(s, t):
    mod = 10**9 + 7
    nums=[0]*26

    for ch in s:
        nums[ord(ch)-97]+=1

    for _ in range(t):
        cur=[0]*26
        z=nums[25]

        if z:
            cur[0]=(cur[0]+z)%mod
            cur[1]=(cur[1]+z)%mod
        
        for j in range(25):
            v=nums[j]
            if v:
                cur[j+1]=(cur[j+1]+v)%mod
        
        nums=cur
    
    res=0
    for v in nums:
        res=(res+v)%mod
    return res

print(lengthAfterTransformationsBrute(s, t))
print(lengthAfterTransformationsOptimized(s, t))