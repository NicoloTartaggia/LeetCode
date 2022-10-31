import math
from turtle import st

class Solution:
    def calculate(self, s: str):
        stack = []
        i, tmp = 0, 0
        op = '+'
        while i < len(s):
            if s[i].isdigit():
                tmp = tmp*10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1: 
                if op == '-':
                    stack.append(int(tmp)*(-1))
                elif op == '+':
                    stack.append(int(tmp))
                elif op == '*':
                    stack.append(stack.pop()*tmp)
                elif op == '/':
                    stack.append(int(stack.pop()/tmp))
                tmp = 0
                op = s[i]
            i += 1
        return sum(stack)

print(Solution().calculate("14-3/2"))