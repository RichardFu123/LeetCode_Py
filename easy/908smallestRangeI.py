class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return 0 if (max(A) - min(A) - 2 * K)<=0 else (max(A) - min(A) - 2 * K)s
