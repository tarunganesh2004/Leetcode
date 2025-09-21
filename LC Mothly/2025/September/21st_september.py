# Design Movie Rental System LC 1912(Hard)

from collections import defaultdict
from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self,n,entries):
        self.shops=defaultdict(SortedList)
        self.shop_movie={}
        self.rented=SortedList()
        for shop,movie,price in entries:
            self.shops[movie].add((price,shop))
            self.shop_movie[(shop,movie)]=price
    
    def search(self,movie):
        return [y for _,y in self.shops[movie][:5]]
    
    def rent(self,shop,movie):
        price=self.shop_movie[(shop,movie)]
        self.shops[movie].remove((price,shop))
        self.rented.add((price,shop,movie))

    def drop(self,shop,movie):
        price=self.shop_movie[(shop,movie)]
        self.shops[movie].add((price,shop))
        self.rented.remove((price,shop,movie))

    def report(self):
        return [(y,z) for x,y,z in self.rented[:5]]
    
    