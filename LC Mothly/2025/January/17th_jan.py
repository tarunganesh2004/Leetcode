# # Neighboring bitwise XOR LC 2683

# A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in a binary array original of length n.

# Specifically, for each index i in the range [0, n - 1]:

# If i = n - 1, then derived[i] = original[i] ⊕ original[0].
# Otherwise, derived[i] = original[i] ⊕ original[i + 1].
# Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived.

# # Return true if such an array exists or false otherwise.


derived=[1,1,0] # a valid original array is [0,1,0]
# derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
# derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
# derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
# so we return true

# the idea is in the derived array if we xor all elements and the result is 0 then we can form the original array
def doesValidArrayExist(derived):
    ans=0
    for i in range(len(derived)):
        ans^=derived[i]
    return ans==0

# Another approach using sum parity
# the sum of the derived array gives the total count of 1s in the original array
# if the sum is even then we can form the original array
def doesValidArrayExistParity(derived):
    return sum(derived)%2==0

print(doesValidArrayExist(derived)) # True
print(doesValidArrayExistParity(derived)) # True