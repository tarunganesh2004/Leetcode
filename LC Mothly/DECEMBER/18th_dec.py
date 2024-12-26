# LC 1475 Final Prices with a special Discount in a shop
prices=[8,4,6,2,3]

def brute(prices):
    n=len(prices)
    for i in range(n):
        for j in range(i+1,n):
            if prices[j]<=prices[i]:
                prices[i]-=prices[j]
                break
    return prices

def finalPricesOptimized(prices):
    n = len(prices)
    # Initialize a stack to store the indices of the prices
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]]>=prices[i]:
            # Pop the top index from the stack
            idx = stack.pop()
            # Apply the discount
            prices[idx]-=prices[i]

        # Push the current index into the stack
        stack.append(i)
    
    return prices

# print(brute(prices)) # [4, 2, 4, 2, 3]
print(finalPricesOptimized(prices))