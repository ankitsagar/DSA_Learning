

class BinaryMaxHeap:
    """ Max heap/Binary heap/Priority queue implementation. """

    def __init__(self, arr=[]):
        """ Pass a list on intialization to covert it into a max heap """
        self.__size = len(arr)
        self.__heap = arr
        self._heapify()

    def _heapify(self):
        """
        Heapify the current heap, start from the parent of leaf nodes till
        root and use shift_down on every one of them to fix the tree.
        """
        count = int(self.__size / 2)
        while count != 0:
            self._shift_down(count)
            count -= 1

    @staticmethod
    def _get_parent_index(index):
        """ Returns given index's right child index. """
        return int(index/2)

    @staticmethod
    def _get_right_child_index(index):
        """ Returns given index's right child address. """
        return index * 2 + 1

    @staticmethod
    def _get_left_child_index(index):
        """ Returns given index's left child address. """
        return index * 2

    def _shift_up(self, index):
        """
        Shift the element up until the max heap property is satisfied that is
        parent value must be greater than both children.
        """
        if index == 1:  # can't move root further up
            return
        heap = self.__heap
        p_index = self._get_parent_index(index)
        # Since I'm using 0 based indexing need to subtract by 1 to get actual
        # address in the list.
        arr_idx, p_arr_idx = index - 1, p_index - 1
        value = heap[arr_idx]
        parent_value = heap[p_arr_idx]
        if value > parent_value:
            # Swap and repeat...
            heap[arr_idx], heap[p_arr_idx] = heap[p_arr_idx], heap[arr_idx]
            self._shift_up(p_index)

    def _shift_down(self, index):
        """
        Shift the item down utill the max heap property is satisfied that is
        parent value must be greater than both children.
        """
        heap = self.__heap
        lc_index = self._get_left_child_index(index)
        rc_index = self._get_right_child_index(index)
        # Since I'm using 0 based indexing need to subtract by 1 to get actual
        # address in the list.
        arr_idx, lc_arr_idx, rc_arr_idx = index - 1, lc_index - 1, rc_index - 1

        try:
            lc_value = heap[lc_arr_idx]
        except IndexError:
            lc_value = None

        try:
            rc_value = heap[rc_arr_idx]
        except IndexError:
            rc_value = None

        if rc_value and lc_value:
            # If both are the there then check for the worthy child to swap
            if rc_value > lc_value:
                cmp_value, cmp_index, cmp_arr_idx = rc_value, rc_index, rc_arr_idx  # noqa
            else:
                cmp_value, cmp_index, cmp_arr_idx = lc_value, lc_index, lc_arr_idx  # noqa
        elif lc_value:
            cmp_value, cmp_index, cmp_arr_idx = lc_value, lc_index, lc_arr_idx
        elif rc_value:
            cmp_value, cmp_index, cmp_arr_idx = rc_value, rc_index, rc_arr_idx
        else:
            # it's a leaf, can't move further down
            return
        value = heap[arr_idx]
        if value < cmp_value:
            # Swap and repeat...
            heap[arr_idx], heap[cmp_arr_idx] = heap[cmp_arr_idx], heap[arr_idx]
            self._shift_down(cmp_index)

    def insert(self, item):
        self.__heap.append(item)
        self.__size += 1
        self._shift_up(self.__size)

    def get_max(self):
        """ Returns max without removing it. """
        if self.__heap:
            _max = self.__heap[0]
        else:
            _max = None
        return _max

    def get_size(self):
        """ Return number of elements stored. """
        return self.__size

    def is_empty(self):
        """ Returns true if heap contains no elements. """
        if self.__size:
            empty = False
        else:
            empty = True
        return empty

    def extract_max(self):
        """ Returns the max item by removing it. """
        if not self.__size:
            raise IndexError
        heap = self.__heap
        if self.__size - 1:
            _max = heap[0]
            # Copy the last element to root and remove the copy from end then
            # start shifting it down.
            heap[0] = heap[-1]
            del heap[-1]
            self._shift_down(1)
        else:  # Then there is only one element.
            _max = heap.pop()
        self.__size -= 1
        return _max

    def remove(self, index):
        """ Removes the item from index x, index start from 1 for heap. """
        # Make the given index's value infinity, bubble it up to root and then
        # call extract_max to remove :)
        self.__heap[index - 1] = float("inf")
        self._shift_up(index)
        self.extract_max()

    def __repr__(self):
        return str(self.__heap)


def heap_sort(arr):
    """
    Takes the unsorted array in arguments and returns a sorted array using
    heap sort algorithm.
    """
    heap = BinaryMaxHeap(arr=arr)
    return [heap.extract_max() for i in range(heap.get_size())]


if __name__ == "__main__":
    print("=========> Without passing array in __init__ <=========")
    heap = BinaryMaxHeap()
    print("Heap        ====>", heap)
    print("is_empty    ====>", heap.is_empty())
    print("size        ====>", heap.get_size())
    heap.insert(13)
    heap.insert(8)
    heap.insert(9)
    heap.insert(7)
    heap.insert(5)
    heap.insert(3)
    print("========> Insert Done <========")
    print("Heap        ====>", heap)
    print("get_max     ====>", heap.get_max())
    print("size        ====>", heap.get_size())
    print("is_empty    ====>", heap.is_empty())
    print("extract_max ====>", heap.extract_max())
    print("Heap        ====>", heap)
    print("get_max     ====>", heap.get_max())
    print("size        ====>", heap.get_size())
    print("remove(2)   ====>", heap.remove(2))
    print("Heap        ====>", heap)
    print("get_max     ====>", heap.get_max())
    print("size        ====>", heap.get_size())

    print("=========> With array in __init__ <=========")
    arr = [18, 39, 7, 3, 25, 3]
    print("arr passed  ====>", arr)
    heap = BinaryMaxHeap(arr=arr)
    print("Heap        ====>", heap)
    print("is_empty    ====>", heap.is_empty())
    print("size        ====>", heap.get_size())
    print("get_max     ====>", heap.get_max())
    print("extract_max ====>", heap.extract_max())
    print("Heap        ====>", heap)
    print("get_max     ====>", heap.get_max())
    print("size        ====>", heap.get_size())
    print("extract_max ====>", heap.extract_max())
    print("Heap        ====>", heap)
    print("extract_max ====>", heap.extract_max())
    print("Heap        ====>", heap)
    print("extract_max ====>", heap.extract_max())
    print("Heap        ====>", heap)

    # print("============> Heap sort test <===================")
    arr = [2, 4, 53, 45, 25, 77, 33, 3]
    print("sorted arr  ====>", heap_sort(arr))
