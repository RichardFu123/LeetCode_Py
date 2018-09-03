class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(self.generate_valid(n)) if n > 0 else []
        
    def generate_valid(self, n, partial_solution=[], current_open=0):
        if n == 0 and current_open == 0:
            yield "".join(partial_solution)
        else:
            if current_open > 0:
                yield from self.generate_valid(n, partial_solution + [")"], current_open - 1)
            if n > 0:
                yield from self.generate_valid(n - 1, partial_solution + ["("], current_open + 1)
