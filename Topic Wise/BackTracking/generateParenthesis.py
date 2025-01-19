# Generate Parenthesis LC 22

n=3
def generateParenthesis(n):
    s=""
    res=[]
    def backtrack(s,open,close):
        if len(s)==2*n: # if the length of the string is 2*n, then append it to the result
            res.append(s)
            return
        if open<n: # if the number of open brackets is less than n, then add an open bracket
            backtrack(s+"(",open+1,close)
        if close<open: # if the number of close brackets is less than open brackets, then add a close bracket
            backtrack(s+")",open,close+1)
    backtrack(s,0,0)

    return res

print(generateParenthesis(n)) # ["((()))","(()())","(())()","()(())","()()()"]