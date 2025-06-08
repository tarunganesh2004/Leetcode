# Lexicographical Numbers LC 386

n=13

def lexicalOrder(n):
    res = []
    def dfs(num):
        if num > n:
            return
        res.append(num)
        for i in range(10):
            next_num = num * 10 + i
            if next_num <= n:
                dfs(next_num)

    for i in range(1, 10):
        dfs(i)
    
    return res

print(lexicalOrder(n))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]