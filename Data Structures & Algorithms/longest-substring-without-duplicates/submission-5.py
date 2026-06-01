class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        max_len = 0
        left = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in last_seen:
                left = max(left, last_seen.get(ch, 0) + 1)
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)
        return max_len