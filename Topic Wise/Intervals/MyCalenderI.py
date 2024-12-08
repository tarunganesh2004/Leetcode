"""
LC 729. My Calendar I
"""
import bisect
class MyCalendar:
    def __init__(self):
        self.calendar=[]
    
    def book(self,start,end):
        for s,e in self.calendar:
            print("s =",s,"e =",e)
            print("start =",start,"end =",end)
            if start<e and end>s:
                return False
        self.calendar.append((start,end))
        print(self.calendar)
        return True

class MyCalendarIOptimal:
    def __init__(self):
        self.calendar=[]
    
    def book(self,start,end):
        # Using a balanced BST(Red black tree)
        # checking if the new interval overlaps with any existing interval
        # using binary search to find the correct position to insert the new interval

        pos=bisect.bisect_left(self.calendar,(start,end))

        # if there's no overlap with the previous interval
        if pos>0 and start<self.calendar[pos-1][1]:
            return False
        
        # if there's no overlap with the next interval
        if pos<len(self.calendar) and end>self.calendar[pos][0]:
            return False
        
        # if no overlap ,insert the new interval
        self.calendar.insert(pos,(start,end))
        return True

# input
cal=MyCalendar()
print(cal.book(10,20))
print(cal.book(15,25))
print(cal.book(20,30))
