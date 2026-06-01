class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in num_set:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res