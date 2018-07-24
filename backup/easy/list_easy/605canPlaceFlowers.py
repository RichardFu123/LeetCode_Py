class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0
        i=1
        fb=[0]
        for f in flowerbed:
            fb.append(f)
        fb.append(0)
        while i <(len(fb)-1):
            if fb[i]==fb[i+1]==fb[i-1]==0:
                count+=1
                fb[i]=1
            i+=1
        return count>=n
            
