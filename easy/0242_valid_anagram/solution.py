class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}
        
        for c in s:
            sCount[c] = 1 + sCount.get(c, 1)
        for t in t:
            tCount[t] = 1 + tCount.get(t, 1)
        
        return sCount == tCount
            
 
        