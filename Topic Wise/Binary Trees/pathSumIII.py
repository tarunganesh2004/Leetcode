# Path Sum III LC 437(Medium) (K sum paths)
# Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self, arr):
        if not arr or arr[0] == "N":
            return None
        q = []
        root = TreeNode(arr[0])
        i = 1
        q.append(root)
        while i < len(arr) and q:
            node = q.pop(0)
            if i < len(arr) and arr[i] != "N":
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i >= len(arr):
                break
            if i < len(arr) and arr[i] != "N":
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root


class Solution:
    def kSumPathsBruteForce(self, root, k):  # TLE
        if not root:
            return 0
        res = [0]

        def dfs(node, k):
            if not node:
                return
            check(node, k)
            dfs(node.left, k)
            dfs(node.right, k)

        def check(node, k):
            if not node:
                return
            if node.data == k:
                res[0] += 1
            check(node.left, k - node.data)
            check(node.right, k - node.data)

        dfs(root, k)
        return res[0]

    # other approach is to use prefix sum and hashmap

    def __init__(self):
        self.count = 0

    def sumK(self, root, k):
        dic = {0: 1}

        def dfs(root, k, dic, curSum):
            if not root:
                return
            curSum += root.data
            if curSum - k in dic:
                self.count += dic[curSum - k]

            dic[curSum] = dic.get(curSum, 0) + 1

            dfs(root.left, k, dic, curSum)
            dfs(root.right, k, dic, curSum)
            # remove the node which we are not going to visit again
            dic[curSum] -= 1

        dfs(root, k, dic, 0)
        return self.count

    # other approach (similar to map)
    def countKPaths(
        self, root, k
    ):  # O(n) time and O(h) space, h is the height of the tree
        prefix_sums = {}
        return self.countPathsUtil(root, k, 0, prefix_sums)

    def countPathsUtil(self, node, k, cur_sum, prefix_sums):
        if not node:
            return 0
        pathCount = 0
        cur_sum += node.data
        if cur_sum == k:
            pathCount += 1
        if cur_sum - k in prefix_sums:
            pathCount += prefix_sums[cur_sum - k]

        # add the current sum to the prefix sum
        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

        pathCount += self.countPathsUtil(node.left, k, cur_sum, prefix_sums)
        pathCount += self.countPathsUtil(node.right, k, cur_sum, prefix_sums)

        # remove the current sum from the prefix sum
        prefix_sums[cur_sum] -= 1

        return pathCount

    def printKsumPaths(self, root, k):
        def printPath(node, k, path):
            if not node:
                return
            path.append(node.data)
            printPath(node.left, k, path)
            printPath(node.right, k, path)
            f = 0
            for i in range(len(path) - 1, -1, -1):
                f += path[i]
                if f == k:
                    print(path[i:])
            path.pop()

        printPath(root, k, [])


arr = [8, 4, 5, 3, 2, "N", 2, 3, -2, "N", 1]
root = TreeNode(arr)
root = root.buildTree(arr)
sol = Solution()
print(sol.kSumPathsBruteForce(root, 7))  # 3
print(sol.sumK(root, 7))  # 3

print(sol.countKPaths(root, 7))  # 3

sol.printKsumPaths(root, 7)
