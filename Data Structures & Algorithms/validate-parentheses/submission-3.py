class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        symbols = collections.defaultdict(str)
        symbols.update({'{':'}', '(':')', '[':']'})

        for c in s:
            if stack:
                if c == symbols[stack[-1]]:
                    stack.pop()
                    continue
            
            stack.append(c)
        if len(stack) != 0:
            return False
        return True