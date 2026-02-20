class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Deposit amount must be non-negative")
        if self._size + n > self._capacity:
            raise ValueError(f"Cannot deposit {n}, only {self._capacity - self._size} space left")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Withdraw amount must be non-negative")
        if self._size - n < 0:
            raise ValueError(f"Maximum withdraw is {self._size}")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError(f"Cannot set size to {size}, capacity is {self.capacity}")
        self._size = size

