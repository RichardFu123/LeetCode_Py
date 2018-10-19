class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        halfLenA = int(len(A)/2)
        sortedA = sorted(A,key = lambda x:x%2)
        for i in range(halfLenA):
            res.append(sortedA[i])
            res.append(sortedA[halfLenA+i])
        return res
