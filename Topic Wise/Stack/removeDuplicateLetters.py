# Remove Duplicate Letters LC 316
# goal is to remove duplicate letters and form smallest lexicographical string

s="bcabc"
s1="cbacdcbc"

def removeDuplicateLetters(s):
    # create a dictionary to store the last index of each character
    last_index={char:i for i,char in enumerate(s)}
    # print(last_index)
    # create a set to store the characters in the stack
    seen=set()

    # use monotonic stack
    stack=[]
    for i,char in enumerate(s):
        # if the character is already in the stack then skip
        if char in seen:
            continue

        # if the character is less than the top of the stack and the top of the stack is not the last index
        # then pop the stack
        while stack and char<stack[-1] and i<last_index[stack[-1]]:
            seen.remove(stack.pop())
        
        # add the character to the stack
        stack.append(char)
        seen.add(char)
    
    return "".join(stack)


print(removeDuplicateLetters(s))