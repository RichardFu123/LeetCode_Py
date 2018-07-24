class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo=0
        hi=len(A)-1
        mi=int(hi/2)
        while A:
            if A[mi]>A[mi-1] and A[mi]>A[mi+1]:
                return mi
            if A[mi]<A[mi+1]:
                lo=mi
                mi=int((lo+hi)/2)
            else:
                hi=mi
                mi=int((lo+hi)/2)
                
