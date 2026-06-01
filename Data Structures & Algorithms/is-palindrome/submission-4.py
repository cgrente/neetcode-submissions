class Solution:
    def isPalindrome(self, s: str) -> bool:    
        s_arr = list(s)
        s_arr = [ch for ch in s_arr if ch.isalnum()]
        s = "".join(s_arr).lower()

        left = 0
        rigth = len(s)-1
        print(s)
        while left <= rigth:
            if s[left] == s[rigth]:
                left += 1
                rigth -= 1
                continue
            else:
                return False
            
        # print(s[left])
        # print(s[rigth])

        return True;