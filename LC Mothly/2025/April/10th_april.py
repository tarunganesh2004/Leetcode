# Count the Number of Powerful Integers LC 2999

start=1
finish=6000
limit=4
s="124"

def numberOfPowerfulInt(start,finish,limit,s):
    start_=str(start-1)
    finish_=str(finish)
    def calculate(x,s,limit):
        if len(x)<len(s):
            return 0
        if len(x)==len(s):
            return 1 if x>=s else 0
        
        suffix=x[len(x)-len(s):]
        cnt=0
        pre_len=len(x)-len(s)
        for i in range(pre_len):
            if limit<int(x[i]):
                cnt+=(limit+1)**(pre_len-i)
                return cnt
            cnt+=int(x[i])*(limit+1)**(pre_len-i-1)

        if suffix>=s:
            cnt+=1
        return cnt
    return calculate(finish_,s,limit)-calculate(start_,s,limit)

print(numberOfPowerfulInt(start,finish,limit,s))  
    