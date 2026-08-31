class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {} 

        for i, char in enumerate(s):
            hashmapS[char] = 1 + hashmapS.get(char, 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        
        return hashmapS == hashmapT

        
