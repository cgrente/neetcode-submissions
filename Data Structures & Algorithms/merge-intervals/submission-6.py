class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged: List[List[int]] = []
        
        intervals = sorted(intervals, key=lambda interval: interval[0])

        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            last: List[int] = merged[len(merged) - 1]
            curr: List[int] = intervals[i]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)
        return merged