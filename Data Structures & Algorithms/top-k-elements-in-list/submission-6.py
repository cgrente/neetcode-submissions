class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        arr = []
        for num, count in counts.items():
            arr.append([count, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res