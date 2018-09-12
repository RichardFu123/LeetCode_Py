class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N,M=len(A), len(A[0]) if A else 0
        
        for r in range(N):
            if A[r][0]==0:
                for c in range(M):
                    A[r][c]=1-A[r][c]
            assert(A[r][0]==1)
        
        base=1
        sm=0
        
        for c in range(M-1,-1,-1):
            cnt=sum(A[r][c] for r in range(N))
            sm+=base*max(cnt,N-cnt)
            base*=2
        
        return sm
