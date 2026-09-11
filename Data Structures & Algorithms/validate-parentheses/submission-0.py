class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketBalance = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in bracketBalance:
                if stack and stack[-1] == bracketBalance[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
                
           