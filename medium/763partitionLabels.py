class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        intervals = {}
        res = []
        for i, c in enumerate(S):
            intervals[c] = (intervals.get(c, (i, i))[0], i) 
                
        cur = intervals[S[0]]
        for c in S:
            if intervals[c][0] > cur[1]: 
                res.append(cur[1] - cur[0] + 1)
                cur = intervals[c]
            elif intervals[c][1] > cur[1]:
                cur = (cur[0], intervals[c][1])
        res.append(cur[1] - cur[0] + 1)
                
        return res
