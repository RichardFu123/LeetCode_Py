class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        return [min(abs(i - ll) for ll in [i for i, e in enumerate(S) if e == C]) for i in range(len(S))]
