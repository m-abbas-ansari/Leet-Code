from collections import deque
class MinStack:
    # Using hint 1: Consider each node in the stack having a minimum value
    # Therefore for each value in stack, we will also store the min uptil the point that value was
    # pushed to the stack
    def __init__(self):
        self.stack = deque()
        self.min = 2**31 - 1

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append((val, self.min)) # appending a tuple
            
    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) != 0:
            self.min = self.stack[-1][1]
        else:
            self.min = 2**31 - 1
     

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()