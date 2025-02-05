# Best Time to buy and sell stock LC 121
# Say you have an array for which the ith element is the price of a given stock on day i.

prices=[7,1,5,3,6,4] 
# o/p: 5, buy on day 2 and sell on day 5, profit=6-1=5
# we cant buy and sell on the same day

# Brute force approach
# idea is to find the maximum profit by comparing the difference between the prices of the stock on different days
def bruteForce(prices): # TLE
    maxProfit=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            p=prices[j]-prices[i]
            if p>maxProfit:
                maxProfit=p
    return maxProfit

# two pointers approach
def twoPointers(prices):
    left=0 # at day 0 left=buy
    right=1 # at day 1 right=sell
    maxProfit=0

    while right<len(prices):
        # profitable 
        if prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            maxProfit=max(maxProfit,profit)
        else:
            left=right # if not profitable, update left to right
        right+=1

    return maxProfit

def onePass(prices):
    minPrice=float('inf')
    maxProfit=0

    for price in prices:
        minPrice=min(minPrice,price)
        maxProfit=max(maxProfit,price-minPrice)
    
    return maxProfit

print(bruteForce(prices))
print(twoPointers(prices))
print(onePass(prices))