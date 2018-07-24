class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic=dict()
        res=[]
        for i in range(len(nums2)):
            for j in nums2[i:]:
                if j>nums2[i]:
                    dic[str(nums2[i])]=j-nums2[i]
                    break
                else:
                    dic[str(nums2[i])]=-1
        for k in nums1:
            if dic[str(k)]>0:
                res.append(k+dic[str(k)])
            else:
                res.append(-1)
        return res
