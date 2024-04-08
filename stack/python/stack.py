class Stack:
    """ A python class representing a stack data structure
    
    Sample text
    """
    def __init__(self, size=-1) -> None:
        self.stack = []
        self.size = size
        
    def push(self, input) -> None:
        self.stack.append(input)
        
    def pop(self) -> None:
        self.stack.pop
        
    def peek(self) -> any:
        return(self.stack[-1])
        
    def isEmpty(self) -> bool:
        return self.stack == []       

    def isFull(self) -> bool:
        if self.size != -1:
            return len(self.stack) == self.size
        return False
    
if __name__ == '__init__':
    