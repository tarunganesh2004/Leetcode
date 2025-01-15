# Daily Temperatures LC 739

temperatures=[73, 74, 75, 71, 69, 72, 76, 73]

# bruteforce approach
def dailyTemperaturesBrute(arr):
    n=len(arr)
    res=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                res[i]=j-i
                break
    return res

# optimal approach is to use monotonic stack
def dailyTemperatures(arr):
    n=len(arr)
    res=[0]*n
    stack=[]
    for i in range(n):
        # print(i,stack)
        
        while stack and arr[i]>arr[stack[-1]]: # if current day is warmer than the day at top of stack
            # print(arr[i], arr[stack[-1]])
            idx=stack.pop() # index of the day which is warmer than current day
            # so the number of days is calculated by dif b/w each day and next warmer day
            # cur_idx-index at each day
            # print(i-idx)
            res[idx]=i-idx
            # print(res)
        stack.append(i) 

    return res

print(dailyTemperaturesBrute(temperatures))
print(dailyTemperatures(temperatures))