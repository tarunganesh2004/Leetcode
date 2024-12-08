"""
LC 729. My Calendar I
"""
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
    
# input
cal=MyCalendar()
print(cal.book(10,20))
print(cal.book(15,25))
print(cal.book(20,30))
