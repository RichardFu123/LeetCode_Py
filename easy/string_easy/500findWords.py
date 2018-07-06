class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        f={'q','w','e','r','t','y','u','i','o','p'}
        s={'a','s','d','f','g','h','j','k','l'}
        t={'z','x','c','v','b','n','m'}
        word=''
        setword=set()
        ns=set()
        res=[]
        for i in words:
            word=i.lower()
            setword=set(word)
            if setword-f==ns or setword-s==ns or setword-t==ns:
                res.append(i)
        return res
