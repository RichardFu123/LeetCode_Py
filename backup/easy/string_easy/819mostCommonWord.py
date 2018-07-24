class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
        
