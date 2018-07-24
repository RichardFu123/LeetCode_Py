class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for i in range(0,len(numbers)):
            sub = target - numbers[i]
            if sub in res.keys():
                return [res[sub]+1,i+1]
            else:
                res[numbers[i]] = i
        return []
