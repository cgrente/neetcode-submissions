class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == None or len(nums) < 2:
            return False
        
        last_seen = set()
        for num in nums:
            if num in last_seen:
                return True
            last_seen.add(num)

        return False