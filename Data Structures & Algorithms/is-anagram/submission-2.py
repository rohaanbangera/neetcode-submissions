class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for c in s:
            if c in d1:
                d1[c] +=1
            else:
                d1[c] = 1
        for x in t:
            if x in d2:
                d2[x] +=1
            else:
                d2[x] = 1
        return d1 == d2