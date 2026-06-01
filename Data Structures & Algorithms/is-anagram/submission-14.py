class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_char = defaultdict()
        for i, _ in enumerate(s):
            counts_char[s[i]] = counts_char.get(s[i], 0) + 1
            counts_char[t[i]] = counts_char.get(t[i], 0) - 1
        for i, ch in enumerate(counts_char):
            if counts_char.get(ch) != 0:
                return False
        return True