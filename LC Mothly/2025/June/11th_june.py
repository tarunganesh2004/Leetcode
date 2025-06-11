# Maximum Difference Between Even and Odd Frequency II  LC 3445

s="12233"
k=4

class FenwickTree:
    INF = float("inf")

    def __init__(self, n):
        self.n = n
        self.tree = [self.INF] * (n + 1)

    def update(self, i, val):
        pos = i + 1
        while pos <= self.n:
            self.tree[pos] = min(self.tree[pos], val)
            pos += pos & -pos

    def query(self, i):
        res = self.INF
        pos = i + 1
        while pos > 0:
            res = min(res, self.tree[pos])
            pos -= pos & -pos
        return res


def maxDifference(s, k):
    n = len(s)
    ans = float("-inf")

    for a in range(5):
        for b in range(5):
            if a == b:
                continue

            D = [0] * (n + 1)
            pa = [0] * (n + 1)
            pb = [0] * (n + 1)
            countB = [0] * (n + 1)

            for i in range(1, n + 1):
                digit = int(s[i - 1])
                D[i] = D[i - 1] + (1 if digit == a else 0) - (1 if digit == b else 0)
                pa[i] = (pa[i - 1] + (1 if digit == a else 0)) & 1
                pb[i] = (pb[i - 1] + (1 if digit == b else 0)) & 1
                countB[i] = countB[i - 1] + (1 if digit == b else 0)

            trees = [[FenwickTree(n + 1) for _ in range(2)] for _ in range(2)]

            for j in range(n + 1):
                if j >= k:
                    idx = j - k
                    trees[pa[idx]][pb[idx]].update(countB[idx], D[idx])

                if j > 0:
                    needP = 1 - pa[j]
                    needQ = pb[j]
                    if countB[j] > 0:
                        bestVal = trees[needP][needQ].query(countB[j] - 1)
                        if bestVal != FenwickTree.INF:
                            ans = max(ans, D[j] - bestVal)

    return ans

print(maxDifference(s, k))  # Output: -1