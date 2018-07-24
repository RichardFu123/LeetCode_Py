class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                dis = (p[0]-q[0]) ** 2 + (p[1]-q[1])**2
                cmap[dis] = cmap.get(dis,0)+1
            for key in cmap:
                res += (cmap[key]) * (cmap[key]-1)
        return res
