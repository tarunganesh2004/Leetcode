# Sum of All Subset XOR Totals LC 1863

nums=[1,3]

def subsetXORSum(nums):
    # backtracking
    def helper(nums,idx,cur_xor):
        if idx==len(nums):
            return cur_xor
        # include current element in the subset
        include =helper(nums,idx+1,cur_xor^nums[idx])
        # exclude current element from the subset
        exclude=helper(nums,idx+1,cur_xor)
        return include+exclude
    return helper(nums,0,0)

print(subsetXORSum(nums))