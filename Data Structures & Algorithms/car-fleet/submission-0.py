class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))

        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)