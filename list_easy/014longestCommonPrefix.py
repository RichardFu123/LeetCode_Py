class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=''
        co=zip(*strs)
        for i in list(co):
            if len(set(i))==1:
                res+=i[0]
            else:
                return res
        return res
