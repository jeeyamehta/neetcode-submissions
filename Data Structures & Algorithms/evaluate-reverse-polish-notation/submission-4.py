class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t.isdigit():
                s.append(int(t))
            elif t[0] == '-' and len(t)>1:
                s.append((int(t[0:])))

            else:

                op = t
                if op == '+':
                    s.append(s.pop()+s.pop())
                elif op == '-':
                    a = s.pop()
                    b = s.pop()
                    s.append(b-a)   
                elif op == '*':
                    s.append(s.pop()*s.pop())      
                elif op == '/':
                    a = s.pop()
                    b = s.pop()
                    s.append(int(b/a))   
        return s[0]                

        