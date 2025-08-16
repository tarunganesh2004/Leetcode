

num=9669

def maximum69Number(num):
    num_str=str(num)
    num_str = num_str.replace('6', '9', 1)
    return int(num_str)

# other approach
def other(num):
    s=str(num)
    for i,c in enumerate(s):
        if c=='6':
            s= s[:i] + '9' + s[i+1:]
            return int(s)
    return num

print(maximum69Number(num))  # Output: 9969
print(other(num))  # Output: 9969