class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        gg=[]
        if not ghosts:
            return True
        for i in ghosts:
            gg.append(abs(i[0]-target[0])+abs(i[1]-target[1]))
        return (abs(target[0])+abs(target[1]))<min(gg)
