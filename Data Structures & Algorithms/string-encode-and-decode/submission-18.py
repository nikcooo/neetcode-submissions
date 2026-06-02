
class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#"+ strs[i] 
            
        return "".join(strs)


    def decode(self, s: str) -> List[str]:
        x =[]
        t = 0
        r = 0

        while t < len(s):
            if s[t] == "#":
                n = (s[r:t])
                t +=1
                n = int(n) 
                x.append(s[t:t+n])
                r = t + n
                t = t + n 
            else : 
                t = t+1      
        return x