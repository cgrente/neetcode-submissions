class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_seen = {}

        for [i, num] in enumerate(nums):
            looking = target - nums[i]
            if looking in last_seen:
                return [last_seen[looking], i]
            last_seen[num] = i
        return []