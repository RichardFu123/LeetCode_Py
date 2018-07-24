class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        li=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a=ord('a')
        word=''
        res=[]
        for i in words:
            word=''
            for j in range(len(i)):
                word+=li[ord(i[j])-a]
            res.append(word)
        return(len(set(res)))
