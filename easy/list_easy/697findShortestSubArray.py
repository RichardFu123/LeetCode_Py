class Solution:
    def findShortestSubArray(self, nums):
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        c = collections.Counter(nums)
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)
