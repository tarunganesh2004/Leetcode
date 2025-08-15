# Largest 3-Same-Digit Number in String LC 2264

num="6777133339"

def largestGoodInteger(num):
    for i in range(9,-1,-1):
        check= str(i) * 3
        if check in num:
            return check
    return ""

print(largestGoodInteger(num))  # Output: "777"