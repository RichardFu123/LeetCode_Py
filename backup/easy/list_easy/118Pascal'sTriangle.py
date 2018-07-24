class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = [[1]]
        for i in range(1,numRows):
            r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
        return r[:numRows]
    
