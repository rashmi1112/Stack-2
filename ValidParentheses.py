# TC: O(N) since we will be iterating over all the characters of the string. 
# SC: O(N) as in worst case, all characters of the input string would be stored in the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0: 
            return True
        
        stack = []
        for i in range(len(s)): 
            if s[i] == '(': 
                stack.append(')')
            elif s[i] =='{': 
                stack.append('}')
            elif s[i] == '[': 
                stack.append(']')
            else: 
                if not stack or stack.pop() != s[i]: 
                    return False
        
        if len(stack): 
            return False
        
        return True
