class Stack:
    """ A python class representing a stack data structure
    
    Sample text
    """
    def __init__(self, max=-1) -> None:
        self.stack = []
        self.max = max
        
    def push(self, input) -> None:
        if len(self.stack) < self.size or self.max < 0:
            self.stack.append(input)
        
    def pop(self) -> None:
        self.stack.pop(-1)
        
    def peek(self) -> any:
        return(self.stack[-1])
        
    def isEmpty(self) -> bool:
        return self.stack == []       

    def isFull(self) -> bool:
        if self.max != -1:
            return len(self.stack) == self.max
        return False
    
    def size(self) -> int:
        return len(self.stack)