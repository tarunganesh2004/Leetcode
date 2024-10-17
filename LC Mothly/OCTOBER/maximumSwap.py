def maxSwap(num):
    num_str=str(num)
    num_str=list(num_str)

    # create a dictionary to store the last index of each digit
    idx=range(len(num_str))
    paired=zip(idx,num_str) # pair the index with the digit
    last={}
    for i,d in paired:
        last[int(d)]=i  # {2:0, 7:1, 3:2, 6:3}
    
    # iterate through the digits
    for i in range(len(num_str)):
        d=int(num_str[i])

        for larger in range(9,d,-1):
            if larger in last and last[larger]>i:
                num_str[i],num_str[last[larger]]=num_str[last[larger]],num_str[i]
                return int(''.join(num_str))
            
    return num


n=2736
print(maxSwap(n))