from linked_list import LinkedListWithTail


class LinkedListQueue:
    """ Queue implemented using linked list, with tail pointer. """

    def __init__(self):
        self.queue = LinkedListWithTail()

    def enqueue(self, value):
        """ Adds value at position at tail. """
        self.queue.push_back(value)

    def dequeue(self):
        """ Returns value and removes least recently added element (front). """
        node = self.queue.pop_front()
        return node.data

    def empty(self):
        """ Queue is empty or not? """
        return self.queue.empty()


class ArrayQueue:
    """ Queue implemented using fixed sized array. """

    def __init__(self, size):
        # Intialize empty list with given range, adding one buffer to indentify
        # if queue is empty or not.
        self.queue = [None for i in range(size)]
        self.size = size
        self.read = 0
        self.write = 0

    def enqueue(self, value):
        """ Adds item at end of available storage. """
        if self.full():
            raise Exception("Queue is full!!")
        self.queue[self.write] = value
        # Increment write pointer to write to next available space
        self.write = (self.write + 1) % self.size

    def dequeue(self):
        """ Returns value and removes least recently added element. """
        if self.empty():
            raise Exception("Queue is empty!!")
        value = self.queue[self.read]
        self.queue[self.read] = None
        # Increment read pointer to read next value
        self.read = (self.read + 1) % self.size
        return value

    def empty(self):
        """ Queue is empty or not? """
        empty = False
        if self.read == self.write:
            empty = True
        return empty

    def full(self):
        """ Is queue full? """
        full = False
        next_write = (self.write + 1) % self.size
        if self.read == next_write:
            full = True
        return full
