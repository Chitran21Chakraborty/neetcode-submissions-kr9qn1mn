class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for token in tokens:
            if token not in "+-*/":
                stk.append(int(token))
            else:
                b = stk.pop()
                a = stk.pop()
                
                if token == "+":
                    stk.append(a + b)
                elif token == "-":
                    stk.append(a - b)
                elif token == "*":
                    stk.append(a * b)
                elif token == "/":
                    stk.append(int(a / b))  # truncate toward zero
        
        return stk[0]