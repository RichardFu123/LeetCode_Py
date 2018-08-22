class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def trans(word):
            dic=dict()
            pattern=''
            code=0
            for i in word:
                if i not in dic:
                    dic[i]=str(code)
                    code+=1
                pattern+=dic[i]
            return pattern
        res=[]
        patt=trans(pattern)
        for i in words:
            if trans(i)==patt:
                res.append(i)
        return res
