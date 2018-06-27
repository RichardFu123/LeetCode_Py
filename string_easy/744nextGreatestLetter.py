class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        li=list(set(letters))
        li.sort()
        mi=[]
        for i in li:
            mi.append(ord(i))
        for i in mi:
            if i > ord(target):
                return chr(i)
        return chr(mi[0])
