# Soup Servings LC 808

n=50

def soupServings(n):
    memo={}
    def dfs(a,b):
        if a<=0 and b<=0:
            return 0.5
        if b<=0:
            return 0
        if a<=0:
            return 1
        
        if (a,b) in memo:
            return memo[(a,b)]
        
        prob_a1= dfs(a-100, b)
        prob_a2= dfs(a-75, b-25)
        prob_a3= dfs(a-50, b-50)
        prob_a4= dfs(a-25, b-75)

        result = (prob_a1 + prob_a2 + prob_a3 + prob_a4) / 4
        memo[(a,b)] = result
        return result
    
    return 1 if n>=4800 else dfs(n, n)

print(soupServings(n))  # Output: 0.625