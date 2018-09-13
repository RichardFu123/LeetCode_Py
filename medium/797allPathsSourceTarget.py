class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, ancs):
            if node == len(graph) - 1:
                res.append(ancs + [node])
                return
            for child in graph[node]:
                dfs(child, ancs + [node])
        
        res = []
        dfs(0, [])
        return res
