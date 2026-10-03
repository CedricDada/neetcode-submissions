class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        symbols = {'{':'}', '(':')', '[':']'}

        for c in s:
            if stack:
                if stack[-1] in symbols and c == symbols[stack[-1]]:
                    stack.pop()
                    continue
            
            stack.append(c)
        if len(stack) != 0:
            return False
        return True