# Merge Two 2D Arrays by summing values

nums1=[[1,2],[2,3],[4,5]] # id:val
nums2=[[1,4],[3,2],[4,1]]

# o/p: [[1,6],[2,3],[3,2],[4,6]]
# sort by id

def mergeArrays(nums1,nums2):
    m1={}
    m2={}
    for i in nums1:
        m1[i[0]]=i[1]
    # print(m1)
    for i in nums2:
        m2[i[0]]=i[1]
    # print(m2)
    res=[]
    for i in sorted(m1.keys()):
        if i in m2:
            res.append([i,m1[i]+m2[i]])
        else:
            res.append([i,m1[i]])
    # print(res)
    for i in sorted(m2.keys()):
        if i not in m1:
            res.append([i,m2[i]])
        else:
            continue # if we add again it leads to duplicates
    
    # sort by id
    res.sort(key=lambda x:x[0])
    return res

print(mergeArrays(nums1,nums2))