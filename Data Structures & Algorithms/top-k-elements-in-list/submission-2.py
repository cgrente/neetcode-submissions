class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq: List[int] = []

        freq_count = {}
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1

        freq_count_sorted = sorted(freq_count.items(), key=lambda kv: kv[1], reverse=True)

        for key, _ in freq_count_sorted:
            most_freq.append(key)
        
        return most_freq[0:k]