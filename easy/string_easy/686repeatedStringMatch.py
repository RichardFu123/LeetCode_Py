class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A)>=len(B)*3:
            if B in A:
                return 1
            else:
                return -1
        i=1
        while len(A)*i<len(B)*3:
            if B in A*i:
                return i
            i+=1
        return -1
