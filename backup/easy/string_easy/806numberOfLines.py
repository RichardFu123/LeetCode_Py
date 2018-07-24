class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        s=[]
        col=0
        count=0
        for i in S:
            s.append(ord(i)-ord("a"))
        for i in s:
            count+=widths[i]
            if count==100:
                col+=1
                count=0
            if count>100:
                col+=1
                count=widths[i]
        return[col+1,count]
