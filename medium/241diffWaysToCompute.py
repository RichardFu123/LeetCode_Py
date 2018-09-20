class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        n = len(input)
        if n == 0:
            return []
        elif input.isdigit():
            return [int(input)]
        dic = {"+":operator.add, "-":operator.sub, "*":operator.mul}
        res = []
        for i in range(n):
            if not input[i].isdigit():
                op = input[i]
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(dic[op](l,r))
        return res
