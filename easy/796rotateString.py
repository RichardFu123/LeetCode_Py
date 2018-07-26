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


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(B)==len(A) and A in B+B


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if len(A)==0:
            return True
        deq=collections.deque(A,maxlen=len(A))
        deqb=collections.deque(B,maxlen=len(B))
        for i in range(len(A)):
            if deq==deqb:
                return True
            deq.rotate(1)
        return False
