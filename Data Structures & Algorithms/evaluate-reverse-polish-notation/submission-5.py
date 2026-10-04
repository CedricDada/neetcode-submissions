class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                print(token)
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    res = val1 + val2
                elif token == '-':
                    res = val1 - val2
                elif token == '*':
                    res = val1 * val2
                elif token == '/':
                    res = int(val1 / val2)
                stack.append(res)
        return stack[-1]


