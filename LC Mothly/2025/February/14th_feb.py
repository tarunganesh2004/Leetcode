# Product of Last K Numbers LC 1352

class ProductOfNumbers:

    def __init__(self):
        self.prefix=[1]

    def add(self,num):
        if num==0:
            self.prefix=[1]
        else:
            self.prefix.append(self.prefix[-1]*num)

    def getProduct(self,k):
        if k>=len(self.prefix):
            return 0
        return self.prefix[-1]//self.prefix[-1-k]
    
p=ProductOfNumbers()
p.add(3)
p.add(0)
p.add(2)
p.add(5)
p.add(4)
print(p.getProduct(2))
print(p.getProduct(3))