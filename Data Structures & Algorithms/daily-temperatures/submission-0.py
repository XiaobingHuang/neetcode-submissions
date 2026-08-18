class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackI, stackT = stack.pop()
                result[stackI] = i - stackI
            stack.append([i, t])
        return result 
        
        