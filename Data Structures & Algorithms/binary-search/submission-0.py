class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check if the nums list is empty
        # sort the nums list
        # create last_seen 
        # create var for the found index
        # create a loop to go through each num in the nums list
        # create a var that will old a temp value that we will search in the last_seen 
        
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1