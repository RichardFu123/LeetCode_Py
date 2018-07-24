class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                if i == len(bits) - 1:
                    return True
                i += 1
        return False
