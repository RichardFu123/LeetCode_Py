class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = {v:i for i,v in enumerate(list1)}
        best,ans = 1e9,[]
        for i,v in enumerate(list2):
            if v in dic1:
                if i+dic1[v] < best:
                    best = i+dic1[v]
                    ans = [v]
                elif i+dic1[v] == best:
                    ans.append(v)
        return ans
