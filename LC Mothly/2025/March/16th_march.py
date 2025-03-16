# Minimum Time to Repair Cars LC 2594


ranks=[4,2,3,1]
cars=10

def repairCars(ranks,cars):
    low,high=1,cars*cars*ranks[0]
    while low<high:
        mid=(low+high)//2
        cars_repaired=sum(int((mid/rank)**0.5) for rank in ranks)

        if cars_repaired<cars:
            low=mid+1
        else:
            high=mid

    return low

print(repairCars(ranks,cars)) # 16