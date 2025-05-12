# Finding 3-digit even numbers LC 2094

digits=[2,1,3,0]

def findEvenNumbers(digits):
    result = []
    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):
                if i != j and j != k and i != k:
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 and num >= 100:
                        result.append(num)
    return sorted(set(result))

print(findEvenNumbers(digits))