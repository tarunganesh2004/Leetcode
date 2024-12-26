# Decode String - LeetCode 394

s="3[ab]10[c]"

def decodeString(s):
    stack=[]

    for i in range(len(s)):
        # if the character is not ']', then add it to the stack
        if s[i]!=']':
            stack.append(s[i])
        
        else:
            # if the character is ']', then pop the stack until '['
            substr=""
            while stack[-1]!='[': # check until the top of the stack is '['
                substr=stack.pop()+substr # pop the stack and add it to the substring
            
            # now pop the '[' from the stack
            stack.pop()

            # now pop the number from the stack
            num=""
            while stack and stack[-1].isdigit(): # check until the top of the stack is a digit
                num=stack.pop()+num # 0+""=0, next 1+"0"=10
            
            # now multiply the substring with the number
            stack.append(int(num)*substr)

    return "".join(stack)

print(decodeString(s))