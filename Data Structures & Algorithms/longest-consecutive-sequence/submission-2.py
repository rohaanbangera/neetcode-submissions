class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0 
        for num in s:
            if (num-1) not in s:
                streak = 1
                curr = num + 1
                while curr in s:
                    streak +=1
                    curr +=1
                res = max(res, streak)
        return res

        