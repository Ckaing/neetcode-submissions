class MinStack:

    def __init__(self):
        self.stack = []
        self.nums = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.nums.keys():
            self.nums[val] +=1
        else:
            self.nums[val] = 1

    def pop(self) -> None:
        self.nums[self.stack[-1]] -= 1
        if self.nums[self.stack[-1]] == 0:
            self.nums.pop(self.stack[-1], None)
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(set(self.nums))
