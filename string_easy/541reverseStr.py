class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return ''.join([s[i:i+k][::-1]+s[i+k:i+k*2] for i in range(len(s))[::k*2]])
