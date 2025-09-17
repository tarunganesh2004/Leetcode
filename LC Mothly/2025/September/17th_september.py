# Design a Food Rating System LC 2353(Medium)


class FoodRatings:
    def __init__(self,foods,cuisines,ratings):
        self.food_map = {}
        self.cuisine_map = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = (cuisine, rating)
            if cuisine not in self.cuisine_map:
                self.cuisine_map[cuisine] = []
            self.cuisine_map[cuisine].append((-rating, food))
        for cuisine in self.cuisine_map:
            self.cuisine_map[cuisine].sort()

    
    def changeRating(self,food,newRating):
        cuisine, oldRating = self.food_map[food]
        self.food_map[food] = (cuisine, newRating)
        self.cuisine_map[cuisine].remove((-oldRating, food))
        self.cuisine_map[cuisine].append((-newRating, food))
        self.cuisine_map[cuisine].sort()

    
    def highestRated(self,cuisine):
        return self.cuisine_map[cuisine][0][1]


foodRatings = FoodRatings(["kimchi","miso","sushi","moussaka","ramen","bulgogi"],
                          ["korean","japanese","japanese","greek","japanese","korean"],
                          [9,12,8,15,14,7])
print(foodRatings.highestRated("korean")) # Output: "kimchi"
foodRatings.changeRating("sushi",16)
print(foodRatings.highestRated("japanese")) # Output: "sushi"
