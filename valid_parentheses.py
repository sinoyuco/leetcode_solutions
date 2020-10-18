class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {'[':']', '{':'}', '(':')'}
        for i in range(len(s)):
            if s[i] in maps:
                stack.append(maps[s[i]])
            else:
                if stack and s[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
                   
        return True if not stack else False
