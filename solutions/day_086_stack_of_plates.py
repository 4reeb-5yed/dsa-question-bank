class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]
    
    def push(self, val):
        if len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)
    
    def pop(self):
        if not self.stacks[-1]:
            return None
        val = self.stacks[-1].pop()
        if not self.stacks[-1] and len(self.stacks) > 1:
            self.stacks.pop()
        return val
    
    def pop_at(self, index):
        if index >= len(self.stacks) or not self.stacks[index]:
            return None
        val = self.stacks[index].pop()
        if not self.stacks[index] and len(self.stacks) > 1:
            self.stacks.pop(index)
        return val