class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        oa = ord('a') 
        
        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - oa] += 1 # subtract ascii value to get key for the count
            key = tuple(counts)
            groups.setdefault(key, []).append(s)

        return list(groups.values())