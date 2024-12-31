# Maximum Number of Integers to Choose From a Range I LC 2554


banned=[1,2,3,4,5,6,7]
n=8
maxSum=1

def maxCount(banned,n,maxSum):
    banned_set=set(banned)
    c=0
    sum=0
    for i in range(1,n+1):
        if i in banned_set:
            continue
        if sum+i>maxSum:
            break

        sum+=i
        c+=1
    print(c)


def maxCountBrute(banned,n,maxSum):
    s=set()
    for i in range(1,n+1):
        if i not in banned:
            s.add(i)
    # print(s)

    sor=sorted(s)
    c=0
    for i in sor:
        if i<=maxSum:
            c+=1
            maxSum-=i
        else:
            break
    print(c)

maxCount(banned,n,maxSum)
maxCountBrute(banned,n,maxSum)