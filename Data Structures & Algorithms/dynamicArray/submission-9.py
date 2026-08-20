class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None]*capacity

    def get(self, i: int) -> int:
        return int(self.array[i])

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if None in self.array:
            self.array[self.array.index(None)] = n
        else:
            self.resize()
            self.array[self.array.index(None)] = n


    def popback(self) -> int:
        print(self.array)
        if None in self.array:
            pop_v = self.array[self.array.index(None)-1]
            self.array[self.array.index(None)-1] = None
        else:
            pop_v = self.array[-1]
            self.array[-1] = None
        return pop_v
 
    def resize(self) -> None:
            self.array =  self.array + ([None]*self.capacity)
            self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return sum(1 for x in self.array if x is not None)
        
    
    def getCapacity(self) -> int:
        print(f'array {self.array}, capacity {self.capacity}')
        return self.capacity
