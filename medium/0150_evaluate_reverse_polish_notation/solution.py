from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            stack.append(t)
            if t == '+':
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first + second)
            elif t == '-':
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first - second)
            elif t == '*':
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first * second)
            elif t == '/':
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first / second)
        
        return int(stack.pop())
