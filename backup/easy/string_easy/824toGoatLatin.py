class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        goat=''
        m=['a','e','i','o','u','A','E','I','O','U']
        ma=[]
        ma=S.split(' ')
        
        for i in range(len(ma)):
            if ma[i][0] in m:
                goat+=ma[i]+'ma'+'a'*(i+1)+' '
            else:
                goat+=ma[i][1:]+ma[i][0]+'ma'+'a'*(i+1)+' '
        return goat[:-1]
                
            
