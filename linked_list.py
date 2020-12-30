class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return '%s(data=%r, next_node=%r)' % (self.__class__.__name__,
                                              self.data,
                                              self.next_node)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def _add_node(self, value):
        return Node(value)

    def size(self):
        """ Returns numbers of data elements """
        return self._size

    def empty(self):
        """ Bool returns of data if empty """
        empty = True
        if self.head:
            empty = False
        return empty

    def value_at(self, index):
        """ Returns the value of the nth item (starting at 0 for first) """
        # Index should be within size range
        if index > self._size - 1:
            raise Exception("Index out of bound!!")
        i = 0
        node = self.head
        while i != index:
            node = node.next_node
            i += 1
        return node.data

    def push_front(self, value):
        """ Adds an item to the front of the list """
        node = self._add_node(value)
        current_head_node = self.head
        self.head = node
        node.next_node = current_head_node
        self._size += 1

    def pop_front(self):
        """ Remove front item and return its value """
        if not self.head:
            raise Exception("There is no items in list!!")
        node = self.head
        self.head = node.next_node
        self._size -= 1
        return node

    def push_back(self, value):
        """ Adds an item at the end """
        new_node = self._add_node(value)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = new_node
        self._size += 1

    def pop_back(self):
        """ Removes end item and returns its value """
        if not self.head:
            raise Exception("There is no items in list!!")
        node = self.head
        # If there is only one item then make only head null otherwise iterate
        # through all and find out the node before last node and make the next_node
        # pointer null
        if not node.next_node:
            self.head = None
        else:
            while node.next_node.next_node:
                node = node.next_node
            last_node = node.next_node
            node.next_node = None
        self._size -= 1
        return last_node

    def front(self):
        """ Get value of front item """
        value = None
        node = self.head
        if node:
            value = node.data
        return value

    def back(self):
        """ Get value of end item """
        value = None
        node = self.head
        if node:
            while node.next_node:
                node = node.next_node
            value = node.data
        return value

    def insert(self, index, value):
        """
        Insert value at index, so current item at that index is pointed to
        by new item at index
        """
        # Index should be within size range
        if index > self._size:
            raise Exception("Index out of bound!!")
        # if it's at first index then assign to head
        if index == 0:
            self.push_front(value)
        else:
            i = 0
            node = self.head
            while i != index - 1:
                node = node.next_node
                i += 1
            new_node = self._add_node(value)
            new_node.next_node = node.next_node
            node.next_node = new_node
            self._size += 1

    def erase(self, index):
        """ Removes node at given index """
        if index > self._size - 1:
            raise Exception("Index out of bound!!")
        if index == 0:  # Then head needs to be removed
            self.pop_front()
        elif index == self._size - 1:  # Then tail needs to be removed
            self.pop_back()
        else:
            i = 0
            node = self.head
            while i != index - 1:
                node = node.next_node
                i += 1
            node.next_node = node.next_node.next_node
            self._size -= 1

    def value_n_from_end(self, n):
        """
        Returns the value of the node at nth position from the end of the list
        0 is taken as startin index that will be the end and so on.
        """
        index_from_start = self.size - n - 1
        if index_from_start < 0:
            raise Exception("Index out of bound!!")
        i = 0
        node = self.head
        while i == index_from_start:
            node = node.next_node
            i += 1
        return node.data

    def reverse(self):
        """ Reverses the list """
        if self._size in (0, 1):
            return

        node = self.head.next_node
        self.head.next_node = None
        while node is not None:
            next_node = node.next_node
            node.next_node = self.head
            self.head = node
            node = next_node

    def remove_value(self, value):
        """ Removes the first item in the list with this value """
        node = self.head
        if node:
            while node.next_node.next_node:
                if node.next_node.data == value:
                    break
                node = node.next_node
            if not node.next_node.data == value:
                raise Exception(F"{value} not found in the list!!")
            else:
                node.next_node = node.next_node.next_node
            self._size -= 1
        else:
            raise Exception(F"{value} not found in the list!!")

    def __repr__(self):
        start = "["
        end = "]"
        elements = ""
        i = 0
        node = self.head
        while i < self._size:
            elements = elements + str(node.data)
            if not i == self._size - 1:
                elements += ", "
            node = node.next_node
            i += 1
        elements = elements.rstrip()
        return start + elements + end


class LinkedListWithTail:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def _add_node(self, value):
        return Node(value)

    def size(self):
        """ Returns numbers of data elements """
        return self._size

    def empty(self):
        """ Bool returns of data if empty """
        empty = True
        if self.head:
            empty = False
        return empty

    def value_at(self, index):
        """ Returns the value of the nth item (starting at 0 for first) """
        # Index should be within size range
        if index > self._size - 1:
            raise Exception("Index out of bound!!")

        if index == 0:  # Then head needed
            return self.head.data

        if index == self._size - 1:  # Then tail needed
            return self.tail.data

        i = 0
        node = self.head
        while i != index:
            node = node.next_node
            i += 1
        return node.data

    def front(self):
        """ Get value of front item """
        value = None
        node = self.head
        if node:
            value = node.data
        return value

    def back(self):
        """ Get value of end item """
        value = None
        node = self.tail
        if node:
            value = node.data
        return value

    def push_front(self, value):
        """ Adds an item to the front of the list """
        node = self._add_node(value)
        # If there are no items then head and tail will be same.
        if not self.head:
            self.tail = node
        current_head_node = self.head
        self.head = node
        node.next_node = current_head_node
        self._size += 1

    def pop_front(self):
        """ Remove front item and return its value """
        if not self.head:
            raise Exception("There is no items in list!!")
        node = self.head
        self.head = node.next_node
        # If not head then list is empty tail also needs to be cleared.
        if not self.head:
            self.tail = None
        self._size -= 1
        return node

    def push_back(self, value):
        """ Adds an item at the end """
        new_node = self._add_node(value)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self._size += 1

    def pop_back(self):
        """ Removes end item and returns its value """
        if not self.head:
            raise Exception("There is no items in list!!")
        node = self.head
        # If there is only one item then make only head null otherwise iterate
        # through all and find out the node before last node and make the next
        # node pointer null
        if not node.next_node:
            self.head = None
            self.tail = None
        else:
            while node.next_node.next_node:
                node = node.next_node
            last_node = node.next_node
            node.next_node = None
            self.tail = node
        self._size -= 1
        return last_node

    def insert(self, index, value):
        """
        Insert value at index, so current item at that index is pointed to
        by new item at index
        """
        # Index should be within size range
        if index > self._size:
            raise Exception("Index out of bound!!")
        # if it's at first index then assign to head
        if index == 0:
            self.push_front(value)
        elif index == self._size:  # Then it's a push back
            self.push_back(value)
        else:
            i = 0
            node = self.head
            while i != index - 1:
                node = node.next_node
                i += 1
            new_node = self._add_node(value)
            new_node.next_node = node.next_node
            node.next_node = new_node
            self._size += 1

    def erase(self, index):
        """ Removes node at given index """
        if index > self._size - 1:
            raise Exception("Index out of bound!!")
        if index == 0:  # Then head needs to be removed
            self.pop_front()
        elif index == self._size - 1:  # Then tail needs to be removed
            self.pop_back()
        else:
            i = 0
            node = self.head
            while i != index - 1:
                node = node.next_node
                i += 1
            node.next_node = node.next_node.next_node
            self._size -= 1

    def value_n_from_end(self, n):
        """
        Returns the value of the node at nth position from the end of the list
        0 is taken as startin index that will be the end and so on.
        """
        index_from_start = self.size - n - 1
        if index_from_start < 0:
            raise Exception("Index out of bound!!")
        if n == 0:
            node = self.tail
        else:
            i = 0
            node = self.head
            while i == index_from_start:
                node = node.next_node
                i += 1
        return node.data

    def reverse(self):
        """ Reverses the list """
        if self._size in (0, 1):
            return

        current_head = self.head  # It will become tail in the end
        node = self.head.next_node
        self.head.next_node = None
        while node is not None:
            next_node = node.next_node
            node.next_node = self.head
            self.head = node
            node = next_node
        self.tail = current_head

    def remove_value(self, value):
        """ Removes the first item in the list with this value """
        node = self.head
        if node:
            if node.data == value:  # Then head has the value remove it
                self.pop_front()
            while node.next_node.next_node:
                if node.next_node.data == value:
                    break
                node = node.next_node
            if not node.next_node.data == value:
                raise Exception(F"{value} not found in the list!!")
            else:
                if node.next_node == self.tail:
                    self.tail = node
                node.next_node = node.next_node.next_node
            self._size -= 1
        else:
            raise Exception(F"{value} not found in the list!!")

    def __repr__(self):
        start = "["
        end = "]"
        elements = ""
        i = 0
        node = self.head
        while i < self._size:
            elements = elements + str(node.data)
            if not i == self._size - 1:
                elements += ", "
            node = node.next_node
            i += 1
        elements = elements.rstrip()
        return start + elements + end
