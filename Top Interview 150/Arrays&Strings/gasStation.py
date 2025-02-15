# Gas Station LC 134

gas=[1,2,3,4,5]

cost=[3,4,5,1,2]

def canCompleteCircuit(gas,cost):
    n=len(gas)
    totalGas=0
    totalCost=0
    start=0
    tank=0

    for i in range(n):
        totalGas+=gas[i]
        totalCost+=cost[i]
        tank+=gas[i]-cost[i]
        # if we run out of gas,reset start position
        if tank<0:
            start=i+1
            tank=0
    # if total gas is less than total cost,return -1
    if totalGas<totalCost:
        return -1
    return start

print(canCompleteCircuit(gas,cost))