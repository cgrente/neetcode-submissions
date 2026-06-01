from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile / mid)
            
            if total_hours <= h:
                # speed is fast enough, try slower
                right = mid
            else:
                # too slow, go faster
                left = mid + 1

        return left