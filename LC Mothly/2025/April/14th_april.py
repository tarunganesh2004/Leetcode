# Count Good Triplets LC 1534

arr=[3,0,1,1,9,7]
a=7
b=2
c=3

def brute_force(arr,a,b,c):
    cnt=0
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                    cnt+=1

    return cnt

print(brute_force(arr,a,b,c))