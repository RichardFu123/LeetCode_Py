class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        flag=True
        for i in range(left,right+1):
            for j in str(i):
                
                if int(j)==0 or i%int(j)!=0:
                    flag=False
            if flag:
                res.append(i)
            flag=True
        return res
            
