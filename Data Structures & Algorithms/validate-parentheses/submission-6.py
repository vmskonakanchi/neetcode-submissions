class Solution:
    def isValid(self, s: str) -> bool:
        params = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for c in s:
            if c in params:
                if stack and params[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0