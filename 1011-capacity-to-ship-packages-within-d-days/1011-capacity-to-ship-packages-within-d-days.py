class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weights = sum(weights)
        left, right = math.ceil(total_weights / days), total_weights

        def canBeShiped(capacity, days):
            days_used = 1
            remain = capacity
            for weight in weights:
                if weight > capacity:
                    return False
                    
                if remain >= weight:
                    remain -= weight
                else:
                    remain =   capacity - weight
                    days_used += 1

                if days_used > days:
                    return False
            
            return True
                


        while left <= right:
            mid = (left + right) // 2

            if canBeShiped(mid, days):
                right = mid - 1
            else:
                left = mid + 1

        return left


