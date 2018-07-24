class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(B)!=len(A):
            return False
        if A in B+B:
            return True
        return False
        #return len(B)==len(A) and A in B+B
