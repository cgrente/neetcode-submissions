class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_char = [0] * 26
        for i in range(len(s)):
            counts_char[ord(s[i]) - ord('a')] += 1
            counts_char[ord(t[i]) - ord('a')] -= 1
        
        return all(count == 0 for count in counts_char)