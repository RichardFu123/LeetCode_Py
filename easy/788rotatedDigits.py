class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s=''
        res=0
        flag1=True
        flag2=False
        f1=['3','4','7']
        f2=['2','5','6','9']
        for i in range(1,N+1):
            s=str(i)
            for S in s:
                if S in f1:
                    flag1=False
                if S in f2:
                    flag2=True
            if flag1 and flag2:
                res+=1
            flag1=True
            flag2=False
        return res
                    
