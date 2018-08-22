class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res=[]
        s=A+' '+B
        sp=s.split(' ')
        count=collections.Counter(sp)
        for i in count:
            if count[i]==1:
                res.append(i)
        return res
