class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = list(zip(position, speed))
        pos.sort(reverse = True)
        t = []
        stack = []
        for a, b in pos:
            t.append((target - a) / b)
        for i in t:
            if not stack:
                stack.append(i)
            if i > stack[-1]:
                stack.append(i)
        return len(stack)


