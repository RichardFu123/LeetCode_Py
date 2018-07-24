class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars[:] = re.sub(r'(?<=(.))\1+', lambda m: str(1 + len(m.group())), ''.join(chars))
        return len(chars)
