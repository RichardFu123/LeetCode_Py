class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>=1:
            if n%2==1:
                count+=1
            n=int(n/2)
        return count
