class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.__check_full()
        self.array[self.size] = n
        self.size += 1

    def __check_full(self) -> None:
        if self.size == self.capacity:
            self.resize()

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.array[i]

        self.array = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
