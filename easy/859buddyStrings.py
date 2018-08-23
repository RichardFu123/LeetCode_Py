class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        index = []
        for i, v in enumerate(zip(A,B)):
            if v[0] != v[1]:
                index.append(i)
        if len(set(A)) == len(set(B)) == 1 and len(A) == len(B) >= 2:
            return True
        elif (len(index) == 2) and (A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]]):
            return True
        elif len(index) > 2:
            return False
        elif (len(A) == len(B)) and (len(set(A)) == len(set(B)) != len(B)):
            return True
        else:
            return False
