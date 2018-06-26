class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        list1=[]
        res=[]
        for i,x in enumerate(nums):
            list1.append([i,x])
        list1.sort(key=lambda x:x[1])
        try:
            list1[-1][1]="Gold Medal"
            list1[-2][1]="Silver Medal"
            list1[-3][1]="Bronze Medal"
            for i in range(len(list1)):
                list1[i][1]=str(len(list1)-i)
            list1[-1][1]="Gold Medal"
            list1[-2][1]="Silver Medal"
            list1[-3][1]="Bronze Medal"
        except:
            pass
        list1.sort(key=lambda x:x[0])
        for i in list1:
            res.append(i[1])
        return res
