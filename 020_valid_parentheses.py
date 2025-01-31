class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                # print("first case, before", stack)
                stack.append(c)
                # print("first case, after", stack)
            else:
                # print("second case, before", stack)
                if not stack or \
                    (c==')' and stack[-1] != '(') or \
                    (c=='}' and stack[-1] != '{') or \
                    (c==']' and stack[-1] != '['):
                    return False
                stack.pop()
                # print("second case, after", stack)
        return not stack
        
