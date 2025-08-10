# Reordered Power of Two LC 869

n=1

def reorderedPowerOf2(n):
    
    def isPowerOfTwo(x):
        return (x & (x - 1)) == 0
    
    digits = sorted(str(n))
    
    for i in range(31):  # Check powers of 2 up to 2^30
        power_of_two = 1 << i  # This is 2^i
        if sorted(str(power_of_two)) == digits:
            return True
            
    return False

print(reorderedPowerOf2(n))  # Output: True