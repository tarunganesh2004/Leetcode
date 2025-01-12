# # Check if a parentheses String can be valid LC 2116
# # You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.

s="))()))"
locked="010100"

def canBeValid(s,locked):
    n=len(s)

    # if length of string is odd, it can never be a valid string
    if n%2!=0:
        return False
    
    open_brackets=[]
    unlocked=[]
    for i in range(n):
        if locked[i]=="0":
            unlocked.append(i) # store the index of unlocked brackets
        elif s[i]=="(":
            open_brackets.append(i)
        elif s[i]==")":
            if open_brackets:
                open_brackets.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False
            
    # match remaining open brackets with unlocked brackets
    while open_brackets and unlocked and open_brackets[-1]<unlocked[-1]:
        open_brackets.pop()
        unlocked.pop()
    
    if open_brackets:
        return False
    
    return True

print(canBeValid(s,locked)) # True