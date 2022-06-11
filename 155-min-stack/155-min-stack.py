class MinStack:
    # Maintain a parallel stack of minimum values found uptil that point
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = 2**31 - 1

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.min_stack.append(self.min)
        self.stack.append(val)
            
    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.pop()
        if val == self.min:
            if len(self.stack) != 0:
                self.min = self.min_stack[-1]
            else:
                self.min = 2**31 - 1
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()