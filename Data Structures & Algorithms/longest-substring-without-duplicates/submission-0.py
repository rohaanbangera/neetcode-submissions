class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        for i in range(len(s)):
            t = set()
            for j in range(i,len(s)):
                if s[j] in t:
                    break
                t.add(s[j])
            res = max(res,len(t))
        return res