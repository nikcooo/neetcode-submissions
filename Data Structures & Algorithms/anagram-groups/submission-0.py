from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = 0
        x = []
        dict ={}
        while t < len(strs):
            v = tuple(sorted(Counter(strs[t]).items()))
            
            if v in dict :
                dict[v] += (strs[t],)
            else :
                dict[v] = (strs[t],)
            t=t+1
        for r in dict :
            x.append(list((dict[r])))
        return x
        