# LC 17 Letter Combinations of a Phone Number


digits="23"

def letterCombinations(digits):
    if not digits:
        return []
    
    phone=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"] # 0,1 are empty

    res=[]
    def backtrack(start,path):
        if len(path)==len(digits):
            s="".join(path)
            res.append(s)
            return
        
        for i in range(start,len(digits)):
            for j in phone[int(digits[i])]:
                # print(j,end=" ")
                # print(start,path)
                backtrack(i+1,path+[j])
                

    backtrack(0,[])
    return res

def anotherApproach(digits):
    res=[]
    digitToChar={"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
    def backtrack(i,curStr):
        if len(curStr)==len(digits):
            res.append(curStr)
            return
        
        for c in digitToChar[digits[i]]:
            backtrack(i+1,curStr+c)
    
    if digits:
        backtrack(0,"")
    
    return res


print(letterCombinations(digits)) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(anotherApproach(digits)) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']