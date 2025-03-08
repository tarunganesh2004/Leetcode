# Minimum Recolors to Get K Consecutive Black Balls LC 2379

blocks="WBBWWBBWBW"
k=7

def minColors(blocks,k):
    left=0
    num_whites=0
    num_recolors=float('inf')

    for right in range(len(blocks)):
        if blocks[right]=='W':
            num_whites+=1

        if right-left+1==k:
            num_recolors=min(num_recolors,num_whites)
            if blocks[left]=='W':
                num_whites-=1
            left+=1
    return num_recolors

print(minColors(blocks,k)) # 3