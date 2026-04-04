class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(':
                stk.append(')')
            elif c == '{':
                stk.append('}')
            elif c == '[':
                stk.append(']')
            else:
                if not stk or stk.pop() != c:
                    return False
        return len(stk) == 0 