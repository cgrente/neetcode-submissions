class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_ch = {}
        for c in s:
            count_ch[c] = count_ch.get(c, 0) + 1;
        for c in t:
            if c not in count_ch:
                return False
            count_ch[c] = count_ch.get(c, 0) - 1;
            if count_ch[c] == 0:
                count_ch.pop(c)

        return len(count_ch) == 0