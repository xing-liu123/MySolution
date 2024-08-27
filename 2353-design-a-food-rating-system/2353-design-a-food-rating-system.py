class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.heaps = {}
        self.foodMap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            if not c in self.ratings:
                self.ratings[c] = {}
                self.heaps[c] = []
            self.foodMap[f] = c
            self.ratings[c][f] = r
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodMap[food]
        self.ratings[cuisine][food] = newRating
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            top = self.heaps[cuisine][0]
            r, f = -top[0], top[1]

            if r == self.ratings[cuisine][f]:
                return f
            
            heapq.heappop(self.heaps[cuisine])


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)