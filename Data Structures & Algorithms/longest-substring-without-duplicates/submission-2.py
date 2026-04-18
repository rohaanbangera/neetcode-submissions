class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0 
        # for i in range(len(s)):
        #     t = set()
        #     for j in range(i,len(s)):
        #         if s[j] in t:
        #             break
        #         t.add(s[j])
        #     res = max(res,len(t))
        # return res
        c_set = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l+=1
            c_set.add(s[r])
            res = max(res,r-l +1) 
        return res       