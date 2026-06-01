class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
    
        # long_cons_seq = [nums[0]]
        # long_cons_seq_len = 1
        # for i in range(len(nums) - 1, 1, 1):
        #     curr_nb = nums[i]
        #     if num_set. .get(curr_nb + 1) == True:
        #         long_cons_seq.append(curr_nb)
        #         long_cons_seq_len = len(long_cons_seq)
        #     else:
        #         long_cons_seq.clear()
        #         long_cons_seq.append(nums[i + 1])
        #         long_cons_seq_len = max(long_cons_seq_len, len(long_cons_seq))
                
        for num in nums:
            streak, curr = 0, num
            while curr in num_set:
                streak += 1
                curr += 1
            res = max(res, streak)

        return res