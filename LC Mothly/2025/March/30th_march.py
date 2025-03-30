# Partition Labels LC 763

s="ababcbacadefegdehijhklij"

def partitionLabels(s):
    last={c:i for i,c in enumerate(s)}
    start=0
    end=0
    res=[]
    for i,c in enumerate(s):
        end=max(end,last[c])
        if i==end:
            res.append(end-start+1)
            start=i+1
    return res

print(partitionLabels(s))