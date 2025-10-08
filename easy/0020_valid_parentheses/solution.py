class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append('$')
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False        
            
        return stack[-1] == '$'