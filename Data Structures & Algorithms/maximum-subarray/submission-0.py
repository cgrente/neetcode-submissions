class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr = nums[0]
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sub_arr = max(max_sub_arr, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sub_arr