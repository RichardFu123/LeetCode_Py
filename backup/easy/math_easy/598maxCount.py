class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        miM=m
        miN=n
        for i in range(len(ops)):
            miM=min(miM,ops[i][0])
            miN=min(miN,ops[i][1])
        return miM*miN
