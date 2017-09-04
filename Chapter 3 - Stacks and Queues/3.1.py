#3.1 Three in One: Describe how you could use a single array to implement three stacks. 

class MultiStack:

    def _init_(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1 #why does this happen, and what does it do?
        self.array[self.IndexOfTop(stacknum)] = item
        return value
    
    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self,stack num):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

