class Solution:
    def isValid(self, s: str) -> bool:
        dic = { ")": "(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            else:
                if stack and stack[len(stack)-1] != dic[char]:
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


            
        