class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        b=list(magazine)
        for ch in ransomNote:
            if ch in b:
                b.remove(ch)
            else:
                return False
        return True
