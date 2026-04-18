class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add((nums[i],nums[j],nums[k]))
        # return [list(x) for x in res]
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i -1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l<r:
                ts = a + nums[l] + nums[r]
                if ts > 0:
                    r-=1
                elif ts < 0:
                    l+=1
                else:
                    res.append([a,nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res