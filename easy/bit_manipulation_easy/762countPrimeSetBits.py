class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        bi=''
        res=0
        num=[2,3,5,7,11,13,17,19,23]
        for i in range(L,R+1):
            bi=str(bin(i))[2:]
            if bi.count('1') in num:
                res+=1
        return res
