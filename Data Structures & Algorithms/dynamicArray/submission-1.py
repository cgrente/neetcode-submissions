class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum capacity before resizing
        self.size = 0  # Current number of elements
        self.arr = {}  # Use a dictionary to hold elements

    def get(self, i: int) -> int:
        if i in self.arr:
            return self.arr[i]  # Return the element at index i
        raise IndexError("Index does not exist.")

    def set(self, i: int, n: int) -> None:
        # Set the element at index i to n
        if self.size > i:
            self.arr[i] = n  # Assign value n to index i
        else:
            raise IndexError("Index does not exist.")

    def pushback(self, n: int) -> None:
        # Resize if the array is full
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n  # Add the new element
        self.size += 1  # Increase the size

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Pop from empty array.")
        last_element = self.arr[self.size - 1]  # Get the last element
        del self.arr[self.size - 1]  # Remove the last element
        self.size -= 1  # Decrease the size
        return last_element  # Return the last element

    def resize(self) -> None:
        # Double the capacity
        new_capacity = self.capacity * 2
        self.capacity = new_capacity  # Update the capacity

    def getSize(self) -> int:
        return self.size  # Return the current size

    def getCapacity(self) -> int:
        return self.capacity  # Return the current capacity