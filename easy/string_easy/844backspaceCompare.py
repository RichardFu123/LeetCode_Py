class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        li1 = []
        li2 = [] 
        
        for a in S:
            if a != "#":
                li1.append(a) 
            elif a == "#":
                if len(li1) == 0:
                    pass
                else:
                    li1.pop()
        for a in T:
            if a != "#":
                li2.append(a) 
            elif a == "#":
                if len(li2) == 0:
                    pass
                else:
                    li2.pop()
        
        return li1 == li2
