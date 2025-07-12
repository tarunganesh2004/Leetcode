# The Earliest and Latest Rounds Where Players Compete LC 1900(Hard)

n = 11
firstPlayer = 2
secondPlayer = 4

from functools import lru_cache  # noqa: E402


class Solution:
    def earliestAndLatest(self,n, firstPlayer, secondPlayer):
        @lru_cache(None)
        def dp(n, i, j):
            if i + j == n + 1:
                return (1, 1)
            pairs = n // 2
            other = []
            for k in range(1, pairs + 1):
                left, right = k, n - k + 1
                if left != i and left != j and right != i and right != j:
                    other.append((left, right))
            mid = (n + 1) // 2
            m = (n + 1) // 2
            early, latest = float("inf"), 0
            tot = len(other)
            for mask in range(1 << tot):
                surv = []
                for idx, (left, right) in enumerate(other):
                    if (mask >> idx) & 1:
                        surv.append(right)
                    else:
                        surv.append(left)
                surv.append(i)
                surv.append(j)
                if (n % 2 == 1) and mid != i and mid != j:
                    surv.append(mid)
                surv.sort()
                e1, l1 = dp(m, surv.index(i) + 1, surv.index(j) + 1)
                early = min(early, e1 + 1)
                latest = max(latest, l1 + 1)
            return (early, latest)

        return list(dp(n, firstPlayer, secondPlayer)) 


solution = Solution()
print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))  # Output: [3, 5]