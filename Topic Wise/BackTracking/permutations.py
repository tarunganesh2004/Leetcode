# LC 46 Permutations
# Given a collection of distinct integers, return all possible permutations.

nums=[1,2,3]

def permute(nums):
    res=[]

    def backtrack(path):
        if len(path)==len(nums):
            res.append(path)
            return
        
        for num in nums:
            if num not in path:
                backtrack(path+[num])
            
    backtrack([])
    return res

# if asked in java
# public List<List<Integer>> permute(int[] nums) {
#     List<List<Integer>> res=new ArrayList<>();
#     backtrack(res,new ArrayList<>(),nums);
#     return res;
# }
#
# public void backtrack(List<List<Integer>> res,List<Integer> path,int[] nums){
#     if(path.size()==nums.length){
#         res.add(new ArrayList<>(path));
#         return;
#     }
#     for(int num:nums){
#         if(!path.contains(num)){
#             path.add(num);
#             backtrack(res,path,nums);
#             path.remove(path.size()-1);
#         }
#     }
# }

def anotherApproach(nums):
    res=[]

    # base case
    if len(nums)==1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n=nums.pop() # remove the last element
        p=anotherApproach(nums)
        for pe in p:
            pe.append(n)
        
        res.extend(p)
        nums.append(n)
    
    return res

print(permute(nums))
print(anotherApproach(nums))