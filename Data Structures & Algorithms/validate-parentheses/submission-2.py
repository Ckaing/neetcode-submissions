class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'(', '{', '['}
        close = {')', '}', ']'}
        pairs = {'()', '{}', '[]'}
        for i in s:
            if i in open:
                stack.append(i)
            if i in close:
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if last+i in pairs:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
