class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_ch = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count_ch[s[i]] = count_ch.get(s[i], 0) + 1;
        for i in range(len(t)):
            if t[i] in count_ch:
                count_ch[t[i]] = count_ch.get(t[i], 0) - 1;
                if count_ch[t[i]] == 0:
                    count_ch.pop(t[i])
            else:
                return False
        return len(count_ch) == 0