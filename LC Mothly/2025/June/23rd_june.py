# Sum of K-Mirror Numbers LC 2081(Hard)

k=2
n=5

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(x: str) -> bool:
            return x == x[::-1]

        def to_base_k(x: int, k: int) -> str:
            if x == 0:
                return "0"
            digits = []
            while x:
                digits.append(int(x % k))
                x //= k
            return ''.join(str(x) for x in digits[::-1])

        count = 0
        total_sum = 0
        num = 1

        while count < n:
            base_k_num = to_base_k(num, k)
            if is_palindrome(base_k_num):
                count += 1
                total_sum += num
            num += 1

        return total_sum
solution = Solution()
print(solution.kMirror(k, n))  # Output: 25