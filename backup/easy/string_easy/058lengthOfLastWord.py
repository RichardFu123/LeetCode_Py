class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=s.strip().split(' ')
        return len(lis[-1])
