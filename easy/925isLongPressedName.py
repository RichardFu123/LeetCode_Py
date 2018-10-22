class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        tag = ''
        pName = 0
        for i in range(len(typed)):
            try:
                if typed[i]==name[pName]:
                    pName+=1
                    tag = typed[i]
                elif  typed[i]!=tag:
                    return False
            except:
                pass
        if pName == len(name):
            return True
        else:
            return False
        
