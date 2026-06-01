class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        two_before = 1  # ways to reach step 1
        one_before = 2  # ways to reach step 2

        for i in range(3, n + 1):
            current = one_before + two_before
            two_before = one_before
            one_before = current

        return one_before