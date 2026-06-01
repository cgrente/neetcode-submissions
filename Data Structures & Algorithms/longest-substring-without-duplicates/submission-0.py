class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen: Dict[str, int] = {}

        maxLen = 0
        left = 0
        for right, ch in enumerate(s):
            if ch in lastSeen:
                left = max(left, lastSeen.get(ch, 0) + 1)
            lastSeen[ch] = right

            maxLen = max(maxLen, right - left + 1)

        return maxLen