# Minimum Number of People to Teach LC 1733

n=2
languages=[[1],[2],[1,2]]
friendships=[[1,2],[1,3],[2,3]]

def minimumTeachings(n, languages, friendships):
    s=set()
    for friendship in friendships:
        mp={}
        conm=False 
        for lan in languages[friendship[0]-1]:
            mp[lan]=1
        for lan in languages[friendship[1]-1]:
            if lan in mp:
                conm=True
                break
        if not conm:
            s.add(friendship[0]-1)
            s.add(friendship[1]-1)
    max_cnt=0
    cnt=[0]*(n+1)
    for i in s:
        for lan in languages[i]:
            cnt[lan]+=1
            max_cnt=max(max_cnt,cnt[lan])
    return len(s)-max_cnt

print(minimumTeachings(n, languages, friendships))