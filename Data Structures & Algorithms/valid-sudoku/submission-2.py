class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        t = 0
        s = 0 
        a = 0
        x =[[] for _ in range(9)]
        y =[[] for _ in range(9)] 
        z = {}
        while t < 9 : 

            while s < 9:
                if board[t][s].isdigit() == True : 
                    x[t].append(board[t][s])
                    y[s].append(board[t][s])
                    z.setdefault((t//3, s//3), []).append(board[t][s])
                    s += 1
                else :
                    s +=1
            s = 0
            t += 1
        t = 0
        e = []
        f = []
        for i in range(len(x)):
            f = len(x[i])
            e = len(set(x[i]))
            if e == f :
                pass
            else : 
                return False  
        e = []
        f = []
        for i in range(len(y)):
            f = len(y[i])
            e = len(set(y[i]))
            if e == f :
                pass
            else : 
                return False  
        t = list(z.values())
        e = []
        f = []
        for i in range(len(t)):
            f = len(t[i])
            e = len(set(t[i]))
            if e == f :
                pass 
            else : 
                return False
        return True
  



