class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if target < 0:
        #     return []

        last_seen = {}

        looking = 0
        for i in range(len(nums)):
            looking = target - nums[i]
            if looking in last_seen:
                return [last_seen[looking], i]
            last_seen[nums[i]] = i
        
        return []