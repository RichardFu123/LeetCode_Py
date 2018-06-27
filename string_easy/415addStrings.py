class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j, carry, res = 0, 0, 0, []
        while i < len(num1) or j < len(num2) or carry:
            if i < len(num1):
                carry, i = carry+ord(num1[::-1][i])-48, i+1
            if j < len(num2):
                carry, j = carry+ord(num2[::-1][j])-48, j+1
            res += carry%10,
            carry //= 10 

        return "".join([chr(c+48) for c in res[::-1]])
