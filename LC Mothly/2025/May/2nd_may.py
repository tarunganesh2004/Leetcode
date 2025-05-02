# Push Dominoes LC 838

dominoes= "RR.L"

class Solution:
    def pushDominoes(self,dominoes):
        n = len(dominoes)
        left = [0] * n
        right = [0] * n

        # traverse from left side
        # keep count of 'R' occurennces
        count = 0
        for i in range(n):
            if dominoes[i] == "L" or dominoes[i] == "R":
                count = 0
            left[i] = count
            if dominoes[i] == "R" or count != 0:
                count += 1

        # traverse from right side
        # keep count of 'L' occurennces
        count = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == "R" or dominoes[i] == "L":
                count = 0
            right[i] = count
            if dominoes[i] == "L" or count != 0:
                count += 1

        # print(left)
        # print(right)

        ans = ""
        for i in range(n):
            if left[i] == right[i]:
                ans += dominoes[i]
            else:
                if left[i] == 0 and right[i] != 0:
                    ans += "L"
                elif right[i] == 0 and left[i] != 0:
                    ans += "R"
                elif left[i] > right[i]:
                    ans += "L"
                else:
                    ans += "R"

        return ans

s= Solution()
print(s.pushDominoes(dominoes))  # Output: "RR.L"