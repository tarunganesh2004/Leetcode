# # Find the Punishment Number of an Integer LC 2698

# Given a positive integer n, return the punishment number of n.

# The punishment number of n is defined as the sum of the squares of all integers i such that:

# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.


n=37

def punishmentNumber(n): # O(n^2)
    res=0
    def canPartition(num,target):
        if target<0 or num<target:
            return False
        if num==target:
            return True
        
        return (canPartition(num//10,target-num%10) or canPartition(num//100,target-num%100) or canPartition(num//1000,target-num%1000))
    for cur_num in range(1,n+1):
        square=cur_num*cur_num
        if canPartition(square,cur_num):
            res+=square
    return res


def optimizedWay(n):
    ans=0 # precomputed
    l = [0, 1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]  # noqa: E741
    for i in l:
        if i>n:
            break
        ans+=i*i
    return ans

print(punishmentNumber(n))

print(optimizedWay(n))