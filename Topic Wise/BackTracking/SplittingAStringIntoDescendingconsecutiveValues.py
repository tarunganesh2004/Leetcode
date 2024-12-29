# LC 1849 Splitting a String Into Descending Consecutive Values
# Given a string s, you can split s into one or more substrings such that each substring is a consecutive integer:


s="1234"
s1="050043" # output ["05","004","3"] so true

def splitString(s):
    def dfs(index, prev):
        if index == len(s):
            # If we reach the end, it means the string has been split successfully
            return True

        for i in range(index, len(s)):
            num = int(s[index : i + 1])
            # Ensure the current number is exactly one less than the previous
            if num == prev - 1 and dfs(i + 1, num):
                return True

        return False

    # Try splitting the string with different lengths for the first number
    for i in range(1, len(s)):
        first = int(s[:i])
        if dfs(i, first):
            return True

    return False

print(splitString(s)) # False
print(splitString(s1)) # True