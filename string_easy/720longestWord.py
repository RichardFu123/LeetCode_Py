class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        valids = {''}
        for word in sorted(words):
            if word[:-1] in valids:
                valids.add(word)
        return max(sorted(valids), key=len)
