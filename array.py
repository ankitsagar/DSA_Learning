from ctypes import py_object


class MyArray(object):

    def __init__(self):
        self.SIZE = 0
        self.CAPACITY = 4
        self.arr = self._create(self.CAPACITY)

    def size(self):
        """
        Get the array size
        """
        return self.SIZE

    def capacity(self):
        """
        Get the array capacity
        """
        return self.CAPACITY

    def is_empty(self):
        """
        Check array is empty or not
        """
        return True if self.SIZE else False

    def at(self, index):
        """
        Get element form index
        """
        if not 0 <= index < self.SIZE:
            raise IndexError("Index out of range!!")
        return self.arr[index]

    def push(self, element):
        """
        Push element at end
        """
        # Double the size if array is full
        if self.SIZE == self.CAPACITY:
            self._resize(2 * self.CAPACITY)
        self.arr[self.SIZE] = element
        self.SIZE += 1

    def insert(self, index, item):
        """
        Insert element at given index
        """
        # Allowing till size so item can be inserted to end
        if not 0 <= index <= self.SIZE:
            raise IndexError("Index out of range!!")
        # Double the size if array is full
        if self.SIZE == self.CAPACITY:
            self._resize(2 * self.CAPACITY)

        # Catching index error if tried to insert element at end
        try:
            replaced_val = self.at(index)
        except IndexError:
            # If moving element to end then no need to move elements
            replaced_val = None
        self.arr[index] = item

        if replaced_val:
            self._shift_elements_right(index + 1, replaced_val)
        self.SIZE += 1

    def prepend(self, item):
        """
        Insert element at begining
        """
        if self.SIZE == self.CAPACITY:
            self._resize(2 * self.CAPACITY)
        if self.SIZE:
            replaced_val = self.arr[0]
            self.arr[0] = item
        else:
            # If array is empty then no need to move element
            self.arr[0] = item
            replaced_val = None

        if replaced_val:
            self._shift_elements_right(1, replaced_val)
        self.SIZE += 1

    def _shift_elements_right(self, index, replaced_val):
        """
        shifting all trailing elements right (on insertion opreation)
        """
        for i in range(index, self.SIZE + 1):
            # Make sure it's not accessing the last null element
            if not i == self.SIZE:
                new_replaced_val = self.arr[i]
            self.arr[i] = replaced_val
            replaced_val = new_replaced_val

    def _shift_elements_left(self, index):
        """
        shifting all trailing elements (on deletion operation)
        """
        for i in range(index, self.SIZE):
            self.arr[i] = self.arr[i + 1]

    def pop(self):
        """
        remove from end, return value
        """
        # Cannot pop from empty array
        if not self.SIZE:
            raise IndexError("Index out of range!!")

        item = self.arr[self.SIZE - 1]
        self.arr[self.SIZE - 1] = py_object()
        self.SIZE -= 1
        # Reduce array capacity by half is size is 1/4 of capacity
        if self.SIZE == self.CAPACITY / 4:
            self._resize(self.CAPACITY / 2)
        return item

    def _delete(self, index):
        self.arr[index] = py_object()
        self.SIZE -= 1
        self._shift_elements_left(index)

    def delete(self, index):
        """
        delete item at index, shifting all trailing elements left
        """

        # If there is element in array and index is within range
        if self.SIZE and not 0 <= index < self.SIZE:
            raise IndexError("Index out of range!!")

        self._delete(index)

        # Reduce array capacity by half is size is 1/4 of capacity
        if self.SIZE <= self.CAPACITY / 4:
            self._resize(int(self.CAPACITY / 2))

    def remove(self, item):
        """
        looks for value and removes index holding it
        (even if in multiple places)
        """
        self._remove(0, item)

        # Reduce array capacity by half is size is 1/4 of capacity
        if self.SIZE <= self.CAPACITY / 4:
            self._resize(int(self.CAPACITY / 2))

    def _remove(self, index, value):
        if index == self.SIZE:
            return
        if self.arr[index] == value:
            self._delete(index)
            # There can two adjencent values so after shifting elements to left
            # duplicate will be on the same index that's why decreasing index
            # so in the next statement after increasing it by 1 it will be same
            index -= 1
        index += 1
        self._remove(index, value)

    def find(self, value):
        """
        looks for value and returns first index with that value, -1 if not
        found
        """
        index = -1
        for i in range(self.SIZE):
            if self.arr[i] == value:
                index = i
                break
        return index

    def _resize(self, new_capacity):
        """
        Resize the array capacity
        """
        new_arr = self._create(new_capacity)
        for i in range(self.SIZE):
            new_arr[i] = self.arr[i]  # Copy all items to new array

        self.arr = new_arr  # replace with new array
        self.CAPACITY = new_capacity  # Reset capacity

    def _create(self, capacity):
        return (capacity * py_object)()

    def __len__(self):
        return self.size()

    def __getitem__(self, index):
        return self.at(index)

    def __setitem__(self, index, value):
        # Allowing till size so item can be inserted to end
        if not 0 <= index <= self.SIZE:
            raise IndexError("Index assignment out of range!!")
        self.arr[index] = value
        self.SIZE += 1

    def __repr__(self):
        start = "["
        end = "]"
        elements = ""
        for i in range(self.SIZE):
            elements = elements + str(self.arr[i])
            if not i == self.SIZE - 1:
                elements += ", "
        elements = elements.rstrip()
        return start + elements + end
