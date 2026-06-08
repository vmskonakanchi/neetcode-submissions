class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"*","/","+","-"}
        stack = []

        for token in tokens:
            if token in operators:
                if len(stack) > 1:
                    right = stack.pop()
                    left = stack.pop()
                    expression = f'{left}{token}{right}'
                    result = eval(expression)
                    stack.append(int(result))
            else:
                # we have a number
                stack.append(int(token))

        print(stack)

        return stack[-1]