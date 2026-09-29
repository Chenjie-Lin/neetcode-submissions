class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        import operator

        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = ops[i](num2, num1)
                stack.append(int(result))
        return stack.pop()
