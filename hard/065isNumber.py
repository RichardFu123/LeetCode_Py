class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try: 
            float(s)
        except ValueError: 
            return False
        else: 
            return True
