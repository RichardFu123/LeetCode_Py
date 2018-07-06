class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        digits.reverse()
        for i in range(len(digits)):
            num += digits[i]*(10**i)
        num+=1
        s=str(num)
        result=[]
        for i in range(len(s)):
            result.append(int(s[i]))
        return result
        
