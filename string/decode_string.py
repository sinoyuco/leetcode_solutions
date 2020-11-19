class Solution: 
    def decodeString(self, s: str) -> str:
        result = ''
        stack = []
        for i in s:
            if i == ']':
                temp = ''
                while stack:
                    c = stack.pop()
                    if c == '[':
                        m = ''
                        while stack and stack[-1].isnumeric():
                            m = stack.pop() + m
                        r = int(m)*temp
                        if stack:
                            stack.extend(list(r))
                            break
                        result += r
                    else:
                        temp = c + temp
            else:
                if i.isalpha() and not stack:
                    result+=i
                else:
                    stack.append(i)
        return result