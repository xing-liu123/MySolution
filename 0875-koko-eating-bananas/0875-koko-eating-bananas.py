class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # def canEat(k) -> bool:
        #     return sum((b + k - 1) // k for b in piles) <= h

        # minSpeed = 1
        # maxSpeed = max(piles)

        # while minSpeed <= maxSpeed:
        #     midSpeed = (minSpeed + maxSpeed) // 2

        #     if canEat(midSpeed):
        #         maxSpeed = midSpeed - 1
        #     else:
        #         minSpeed = midSpeed + 1

        # return minSpeed

        minSpeed, maxSpeed = max(sum(piles) // h, 1), max(piles)

        def canEat(speed):
            return sum((pile + (speed - 1)) // speed for pile in piles) <= h

        while minSpeed <= maxSpeed:
            midSpeed = (minSpeed + maxSpeed) // 2

            if canEat(midSpeed):
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1

        return minSpeed