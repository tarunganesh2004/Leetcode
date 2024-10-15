def __4SumII(nums1,nums2,nums3,nums4):
    m={}

    for n1 in nums1:
        for n2 in nums2:
            s=n1+n2

            if s in m:
                m[s]+=1
            else:
                m[s]=1

    res=0

    for n3 in nums3:
        for n4 in nums4:
            t=-(n3+n4)

            if t in m:
                res+=m[t]
    
    return res

a=[1, 2]
b=[-2,-1]
c=[-1, 2]
d=[0, 2]
print(__4SumII(list(a),list(b),list(c),list(d))) # 2