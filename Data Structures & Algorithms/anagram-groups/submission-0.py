class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        counts = {}
        for ch in s1:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in s2:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] == 0:
                del counts[ch]

        return len(counts) == 0

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)
            groups.setdefault(key, []).append(s)

        return list(groups.values())