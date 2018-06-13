class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count=0
        total=set(candies)
        c=collections.Counter(candies)
        for i in total:
            count+=c[i]-1
        if count>=(len(candies)/2):
            return len(total)
        else:
            return int(len(total)+count-len(candies)/2)
