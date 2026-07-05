def calculate(s):
    def helper(s, start, end):
        stack = []
        i = start
        num = 0
        op = '+'
        
        while i < end:
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                pass
            elif c == '(':
                j = i + 1
                depth = 1
                while j < end and depth > 0:
                    if s[j] == '(':
                        depth += 1
                    elif s[j] == ')':
                        depth -= 1
                    j += 1
                num = helper(s, i + 1, j - 1)
                i = j - 1
            elif c in '+-*/)':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                if c == ')':
                    return sum(stack)
                op = c
                num = 0
            i += 1
        
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            stack.append(int(stack.pop() / num))
        
        return sum(stack)
    
    return helper(s, 0, len(s))