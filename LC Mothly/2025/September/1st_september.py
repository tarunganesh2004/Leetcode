# Maximum Average Pass Ratio LC 1792

classes=[[1,2],[3,5],[2,2]]
extraStudents=2

def maxAverageRatio(classes,extraStudents):
    import heapq 
    def gain(p,t):
        return (p+1)/(t+1) - p/t
    
    heap=[(-gain(p,t),p,t) for p,t in classes]
    heapq.heapify(heap)

    for _ in range(extraStudents):
        g,p,t=heapq.heappop(heap)
        p+=1
        t+=1
        heapq.heappush(heap,(-gain(p,t),p,t))

    total=sum(p/t for _,p,t in heap)
    return total/len(classes)

print(maxAverageRatio(classes,extraStudents))