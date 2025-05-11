# Three Consecuitive Odds LC 1550

arr=[2,6,4,1]

def threeConsecutiveOdds(arr):
    for i in range(len(arr)-2):
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
            return True
    return False

print(threeConsecutiveOdds(arr))