# Check if Grid Can be Cut into Sections LC 3394



n=4
rectangles=[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

def canCut(rectangles,dim):
    rectangles.sort(key= lambda rectangle: rectangle[dim])
    n_sections=0
    last_end=0
    for rectangle in rectangles:
        if last_end<=rectangle[dim]:
            n_sections+=1
            if n_sections==3:
                return True
        end=rectangle[dim+2]
        if last_end<end:
            last_end=end
    return False

def checkValidCuts(n,rectangles):
    for dim in range(2):
        if canCut(rectangles,dim):
            return True
    return False

print(checkValidCuts(n,rectangles))