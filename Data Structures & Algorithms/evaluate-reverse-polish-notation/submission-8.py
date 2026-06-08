class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"*","/","+","-"}
        stack = []

        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                result = self.evaluate(left,right,token)
                stack.append(int(result))
            else:
                # we have a number
                stack.append(int(token))

        return stack[-1]

    def evaluate(self,left:int,right:int,op:str):
        if op == "*":
            return left * right
        elif op == "/":
            return int(left / right)
        elif op == "+":
            return left + right
        elif op == "-":
            return left - right
        else:
            raise ValueError("Unsupported operation")