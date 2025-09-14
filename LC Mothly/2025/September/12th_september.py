# Vowels Game in a String LC 3227

s="leetcoder"

def doesAliceWin(s):
    for ch in s:
        if ch in 'aeiou':
            return True
    return False

print(doesAliceWin(s))