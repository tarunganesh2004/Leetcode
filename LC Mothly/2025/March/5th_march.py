# Count Total Number of Colored Cells LC 2579

n=1

def coloredCells(n):
    blue_cells=1
    added=4
    while n-1:
        blue_cells+=added
        added+=4
        n-=1
    return blue_cells

# optimized O(1) solution
def optimized(n):
    return 1+n*(n-1)*2

print(coloredCells(n))
print(optimized(n))