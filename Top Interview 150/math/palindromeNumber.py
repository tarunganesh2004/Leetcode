# Palindrome Number LC 9

x=121

# Method 1
def isPalindrome(x):
    if x<0:
        return False
    else:
        return str(x)==str(x)[::-1]
    
# using reverse integer
def isPalindromeAnother(x):
    if x<0:
        return False
    else:
        rev=0
        temp=x
        while temp>0:
            r=temp%10
            rev=rev*10+r
            temp=temp//10
        return x==rev
    
    
print(isPalindrome(x))
print(isPalindromeAnother(x))