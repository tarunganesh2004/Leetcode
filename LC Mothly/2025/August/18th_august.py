# 24 Game LC 679(Hard)

cards=[4,1,8,7]

def bruteForce(arr):
    # check all possible values for two numbers
    def combine(a,b):
        res=[]
        res.append(a+b)
        res.append(a-b)
        res.append(b-a)
        res.append(a*b)
        if b != 0:
            res.append(a/b)
        if a != 0:
            res.append(b/a)
        return res
    
    # recursive function to check all combinations
    def can_make24(nums):
        if len(nums)==1: # only one number left
            return abs(nums[0]-24) < 1e-6
        
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n): # pick 2 numbers
                a, b = nums[i], nums[j]
                print(f"Combining {a} and {b}")
                rest=[nums[k] for k in range(n) if k != i and k != j]  # remaining numbers
                print(f"Remaining numbers: {rest}")
                for res in combine(a,b):
                    if can_make24(rest + [res]):  # check if we can make 24 with the new list
                        return True
        return False
    
    return can_make24(arr)

# to generate all solutions
def generate(nums,target=24.0):
    items=[(float(x),str(int(x)) if float(x).is_integer() else str(x)) for x in nums]
    solutions=set()
    def combine(a,b):
        (av,ae)=a
        (bv,be)=b # (value, expression)
        res=[]
        res.append((av+bv, f"({ae}+{be})"))
        res.append((av-bv, f"({ae}-{be})"))
        res.append((bv-av, f"({be}-{ae})"))
        res.append((av*bv, f"({ae}*{be})"))
        if bv != 0:
            res.append((av/bv, f"({ae}/{be})"))
        if av != 0:
            res.append((bv/av, f"({be}/{ae})"))
        return res
    
    def dfs(values):
        if len(values) == 1:
            if abs(values[0][0] - target) < 1e-6:
                solutions.add(values[0][1])
            return
        n = len(values)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = values[i], values[j]
                rest = [values[k] for k in range(n) if k != i and k != j]
                for res in combine(a, b):
                    dfs(rest + [res])
    dfs(items)
    return solutions

# optimized
def optimized(nums):
    def dfs(nums):
        if len(nums)==1:
            return abs(nums[0] - 24) < 1e-6
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    a,b= nums[i], nums[j]

                    # create new list without a and b
                    next_nums=[]
                    for k in range(len(nums)):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    # try all operations
                    # addition
                    if dfs(next_nums + [a + b]):
                        return True
                    # subtraction
                    if dfs(next_nums + [a - b]):
                        return True
                    # multiplication
                    if dfs(next_nums + [a * b]):
                        return True
                    # division
                    if b != 0 and dfs(next_nums + [a / b]):
                        return True
        return False
    return dfs(nums)

print(bruteForce(cards))  # Output: True
print(generate(cards))
print(optimized(cards))  # Output: True