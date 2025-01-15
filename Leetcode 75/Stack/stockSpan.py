# Online Stock Span LC 901

prices=[100, 80, 60, 70, 60, 75, 85]

class StockSpanner:
    def __init__(self):
        self.stack=[]
    
    def next(self,price:int)->int:
        span=1
        while self.stack and price>=self.stack[-1][0]:
            span+=self.stack.pop()[1]

        self.stack.append((price,span))
        return span

obj=StockSpanner()
for price in prices:
    print(obj.next(price))

# # bruteforce approach
# def stockspanbrute(arr):
#     n=len(arr)
#     s=[0]*n
#     for i in range(n):
#         s[i]=1 # span of atleast 1(current day itself)
#         # check previous prices 
#         j=i-1
#         while j>=0 and arr[j]<=arr[i]:
#             s[i]+=1
#             j-=1
#     return s

# # using monotonic stack
# def stockspan(arr):
#     n=len(arr)
#     span=[0]*n
#     stack=[]
#     for i in range(n):
#         while stack and arr[i]>=arr[stack[-1]]:
#             stack.pop()
#         if not stack:
#             span[i]=i+1 # all previous days have lower prices
#         else:
#             span[i]=i-stack[-1] 

#         stack.append(i)
#     return span
