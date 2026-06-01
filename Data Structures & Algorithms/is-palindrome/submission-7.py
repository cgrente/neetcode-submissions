class Solution:
    def isPalindrome(self, s: str) -> bool:    
        s_arr = [ch.lower() for ch in s if ch.isalnum()]
        s = "".join(s_arr)

        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True;