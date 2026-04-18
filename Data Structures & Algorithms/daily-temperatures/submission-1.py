class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = []
        # count = 0
        # for i in range(len(temperatures)):
        #     j = i+1
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j+=1
        #         count+=1
        #     if j == len(temperatures):
        #         count = 0 
        #     else:
        #         res.append(count)
        # return res
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t,i])
        return res
