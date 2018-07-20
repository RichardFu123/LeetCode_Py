class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x=0
        connect=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    x+=1
                try:
                    if board[i][j]=='X' and board[i][j+1]=='X':
                        connect+=1
                except:
                    pass
                try:
                    if board[i][j]=='X' and board[i+1][j]=='X':
                        connect+=1
                except:
                    pass
        return x-connect
