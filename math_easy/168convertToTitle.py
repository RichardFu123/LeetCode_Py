class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n != 0:
            result = chr((n-1)%26+65) + result
            n = int((n-1)/26)
        return result
