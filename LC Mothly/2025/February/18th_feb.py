# # Construct Smallest Number from DI String LC 2375

# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

# A 0-indexed string num of length n + 1 is created using the following conditions:

# num consists of the digits '1' to '9', where each digit is used at most once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.

pattern="IIIDIDDD"

def smallestNumber(pattern):
    st=[]
    res=[]
    num=1
    for i in range(len(pattern)+1):
        st.append(num)
        num+=1

        if i==len(pattern) or pattern[i]=='I':
            while st:
                res.append(str(st.pop()))
    return "".join(res)

# using backtracking
def anotherApproach(pattern):
    def backtrack(cur_num,used,path):
        if len(path)==len(pattern)+1:
            return path
        
        # try 1-9
        for i in range(1,10):
            if i in used:
                continue

            # if path is empty, add the number
            if not path:
                used.add(i)
                res=backtrack(i,used,path+str(i))
                if res:
                    return res
                used.remove(i)
                continue

            # if the current number satisfies the pattern
            if(pattern[len(path)-1]=='I' and i>cur_num) or (pattern[len(path)-1]=='D' and i<cur_num):
                used.add(i)
                res=backtrack(i,used,path+str(i))
                if res:
                    return res
                used.remove(i)
        
        return None
    return backtrack(None,set(),"")

print(smallestNumber(pattern))
print(anotherApproach(pattern))