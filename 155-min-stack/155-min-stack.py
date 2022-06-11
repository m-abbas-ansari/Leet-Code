import sys
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31 - 1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
     
            
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min and len(self.stack) > 0:
            self.min = self.stack[0]
            for i in self.stack:
                if i < self.min:
                    self.min = i
        elif len(self.stack) == 0:
            self.min = 2**31 - 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()