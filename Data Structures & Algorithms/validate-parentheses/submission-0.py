class Solution:
    def isValid(self, s: str) -> bool:
        dic = { "]":"[", "}":"{", ")":"(" }
        stack = []
        for e in s:
            if e in dic:
                if stack and stack[-1] == dic[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        return True if not stack else False
            
        