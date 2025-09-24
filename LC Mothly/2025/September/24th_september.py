# Fraction to Recurring Decimal LC 166

numerator=1
denominator=2

def fractionToDecimal(numerator, denominator):
    if numerator==0:
        return "0"
    
    res=[]

    # sign 
    if numerator<0 and denominator>0 or numerator>0 and denominator<0:
        res.append('-')

    n,d=abs(numerator),abs(denominator)

    # integral part
    res.append(str(n//d))
    # remainder 
    r=n%d
    if r==0:
        return ''.join(res)
    
    # if r is not zero,then decimal part exists
    res.append('.')
    rmap={}
    while r!=0:
        if r in rmap:
            res.insert(rmap[r],'(')
            res.append(')')
            break
        rmap[r]=len(res)
        r*=10
        res.append(str(r//d))
        r=r%d
    return ''.join(res)

print(fractionToDecimal(numerator,denominator))