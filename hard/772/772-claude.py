class Solution:
    def calculate(self, s: str) -> int:
        # Time: O(n), Space: O(n)
        def parse(s, i):
            stack = []
            num = 0
            op = '+'
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num, i = parse(s, i+1)
                if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                    if op == '+': stack.append(num)
                    elif op == '-': stack.append(-num)
                    elif op == '*': stack.append(stack.pop() * num)
                    elif op == '/': stack.append(int(stack.pop() / num))
                    op = c
                    num = 0
                if c == ')':
                    break
                i += 1
            return sum(stack), i
        return parse(s, 0)[0]
