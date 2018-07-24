class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for c in S:            
            if c.isdigit():
                for i in range(len(res)):
                    res[i] += c
            else:
                copy = res.copy()
                for i in range(len(res)):
                    res[i] += c.lower()
                for i in range(len(copy)):
                    copy[i] += c.upper()
                res.extend(copy)
            
        return res
