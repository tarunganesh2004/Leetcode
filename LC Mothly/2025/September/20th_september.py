# Implement Router LC 3508

from bisect import bisect_left, bisect_right
from collections import defaultdict, deque


class Router:
    def __init__(self,memoryLimit):
        self.n=memoryLimit
        self.packets=deque([])
        self.destinations=defaultdict(int)
        self.mem=set()
    
    def addPacket(self,s,d,t): # source,destination,timestamp
        packet = (s, d, t)
        if packet in self.mem:
            return False

        self.packets.append(packet)
        self.mem.add(packet)
        self.destinations[d].append(t) # type: ignore

        # remove old values
        if self.n < len(self.packets):
            s, d, t = self.packets.popleft()
            self.mem.remove((s, d, t))
            self.destinations[d].popleft() # type: ignore
        return True
    
    def forwardPacket(self):
        if not self.packets:
            return []
        s,d,t=self.packets.popleft()
        self.mem.remove((s,d,t))
        self.destinations[d].popleft() # type: ignore
        return (s,d,t)
    
    def getCount(self,d,s,e):
        destination=self.destinations[d]
        left=bisect_left(destination,s) # type: ignore
        right=bisect_right(destination,e) # type: ignore
        return right-left
    

