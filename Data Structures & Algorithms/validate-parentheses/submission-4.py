class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for c in s:
            if c in bracket_map: # closing bracket
                if not stack or stack[-1] != bracket_map[c]:
                    return False
                    
                stack.pop()
            else: # opening
                stack.append(c)

        return len(stack) == 0