# Plus One LC 66

digits=[1,2,3]

def plusOne(digits):
    # Method 1
    # s="".join(map(str,digits))
    # s=int(s)+1
    # return [int(i) for i in str(s)]

    # without using string conversion
    l=len(digits)
    k=l-1
    while digits[k]==9:
        digits[k]=0
        if k>0:
            k-=1
        else:
            digits.insert(0,1)
            return digits
    digits[k]+=1
    return digits


print(plusOne(digits))