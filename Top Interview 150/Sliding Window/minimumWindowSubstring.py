# Minimum Window Substring LC 76

s="ADOBECODEBANC"
t="ABC"

def minWindow(s,t):
    if s=="" or t=="":
        return ""
    
    window={}
    countT={}
    for chr in t:
        countT[chr]=countT.get(chr,0)+1
    
    have=0
    need=len(countT)

    res,min_len=[-1,-1],float("inf")

    left=0
    for right in range(len(s)):
        cur_chr=s[right]

        window[cur_chr]=window.get(cur_chr,0)+1

        if cur_chr in countT and window[cur_chr]==countT[cur_chr]:
            have+=1

        while have==need:
            if right-left+1<min_len:
                min_len=right-left+1
                res=[left,right]

            # remove left character from window
            left_chr=s[left]
            window[left_chr]-=1
            if left_chr in countT and window[left_chr]<countT[left_chr]:
                have-=1

            left+=1

    return s[res[0]:res[1]+1]


print(minWindow(s,t)) # BANC