class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count=0
        mylist = []
        for i in range(len(S)):
            if(i == len(S)-1 or S[i]!=S[i+1]):
                if(count>=2):
                    mylist.append([i-count,i])
                count=0
            else:
                count+=1
        return mylist
