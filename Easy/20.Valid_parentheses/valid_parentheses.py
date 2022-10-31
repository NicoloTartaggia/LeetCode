class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop(0)
                if (c == ')' and last != '(') or (c == ']' and last != '[') or (c == '}' and last != '{'):
                    return False
        if len(stack) > 0: 
            return False
        return True