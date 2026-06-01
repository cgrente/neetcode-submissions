class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == None or t == None or len(s) != len(t):
            return False
        
        hashmap = {}
        for i in range(len(s)):
            ch = s[i]
            hashmap[ch] = hashmap.get(ch, 0) + 1
        print(hashmap)

        for i in range(len(t)):
            ch = t[i]
            if ch in hashmap:
                occur = hashmap.get(ch) - 1
                if occur == 0:
                    del hashmap[ch]
                else:
                    hashmap[ch] = occur

        if len(hashmap) == 0:
            return True

        return False
        