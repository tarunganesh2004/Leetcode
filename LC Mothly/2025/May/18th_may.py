# Painting a Grid with Three Different Colors LC 1931

def colorTheGrid(m, n):
    mod = 10**9 + 7
    total = 3**m

    # Generate all valid column patterns
    good = []
    pattern = []
    for i in range(total):
        col = []
        val = i
        valid = True
        for _ in range(m):
            col.append(val % 3)
            val //= 3
        col = col[::-1]
        for j in range(1, m):
            if col[j] == col[j - 1]:
                valid = False
                break
        if valid:
            good.append(i)
            pattern.append(col)

    # Map each good index to its pattern
    index_to_pattern = {i: pattern[k] for k, i in enumerate(good)}

    # Compatibility between two valid columns
    rowValid = [[0] * len(good) for _ in range(len(good))]
    for i in range(len(good)):
        for j in range(len(good)):
            if all(
                index_to_pattern[good[i]][k] != index_to_pattern[good[j]][k]
                for k in range(m)
            ):
                rowValid[i][j] = 1

    # DP table
    dp = [[0] * len(good) for _ in range(n + 1)]
    for i in range(len(good)):
        dp[1][i] = 1

    for col in range(2, n + 1):
        for i in range(len(good)):
            for j in range(len(good)):
                if rowValid[i][j]:
                    dp[col][i] = (dp[col][i] + dp[col - 1][j]) % mod

    return sum(dp[n]) % mod


m = 1
n = 2
print(colorTheGrid(m, n))  
