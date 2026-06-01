class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            # calculate area
            area = min(heights[left], heights[right]) * (right - left)

            # update max_area
            max_area = max(max_area, area)
            # move the shorter side inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area