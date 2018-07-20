# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # SBS={}
        # pl=[]
        # same={}
        # if not points:
        #     return 0
        # if len(points)==1:
        #     return len(points)
        # for p in points:
        #     pl.append([p.x,p.y])
        # pl.sort(key=lambda x:x[0])       
        # for point in itertools.combinations(pl,2):
        #     li=list(point)
        #     if li[1][0]==li[0][0]:
        #         if li[1]==li[0]:
        #             if li[1] in same:
        #                 same[li[1]]+=1
        #             else:
        #                 same[li[1]]=1
        #         if 0 in SBS:
        #             SBS[0]+=1
        #             continue
        #         else:
        #             SBS[0]=1
        #             continue               
        #     slope=(float(li[1][1])-li[0][1])/(li[1][0]-li[0][0])
        #     if slope in SBS:
        #         SBS[slope]+=1
        #     else:
        #         SBS[slope]=1
        # if same:
        #     return int((math.sqrt(max(SBS.values())*8+1)+1)/2)+max(same.values())
        # else:
        #     return int((math.sqrt(max(SBS.values())*8+1)+1)/2)
        points = [(i.x, i.y) for i in points]
        points = list(collections.Counter(points).items())
        if len(points) == 0:
            return 0
        res = max([i[1] for i in points])
        fixed = dict()
        for i in range(len(points)):
            dic = dict()
            for j in range(i+1, len(points)):
                x1, y1 = points[i][0][0], points[i][0][1]
                x2, y2 = points[j][0][0], points[j][0][1]
                k = (y1-y2)/(x1-x2) if x1-x2 != 0 else math.inf
                b = y1-k*x1 if x1-x2 != 0 else x1
                cur = (k, b)
                if cur not in fixed:
                    if cur not in dic:
                        dic[cur] = points[i][1] + points[j][1]
                    else:
                        dic[cur] += points[j][1]
                    res = max(res, dic[(k, b)])
            for d in dic:
                fixed[d] = dic[d]
        return res
