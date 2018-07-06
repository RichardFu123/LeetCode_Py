class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        
        for c in s:
            if c =='(':
                stack.append(')')
            elif c =='[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif stack:
                p = stack.pop()
                if p != c:
                    return False
        if stack:
            return False
        else:
            return True
