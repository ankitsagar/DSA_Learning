
class HashTable:

    def __init__(self):
        self.size = 8
        self.length = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.max_load_factor = 2/3

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return self._get(key)

    def __setitem__(self, key, value):
        self._add(key, value)

    def __delitem__(self, key):
        self._remove(key)

    def __repr__(self):
        start = "{"
        end = "}"
        elements = ""
        for i in range(self.size):
            if self.slots[i] not in (None, ""):
                key = self.slots[i]
                value = self.data[i]
                elements += str(key) + ': ' + str(value) + ", "

        elements = elements[:-2]  # Remove last ', '
        if elements:
            display = start + elements + end
        else:
            display = start + end
        return display

    def _hash(self, key):
        return hash(key) % self.size

    def _increment(self, slot_no):
        return (slot_no + 1) % self.size

    def _resize(self):
        old_slots = self.slots
        old_data = self.data
        self.size *= 2
        self.slots = [None] * self.size
        self.data = [None] * self.size
        for index, key in enumerate(old_slots):
            if key not in ("", None):
                value = old_data[index]
                new_slot = self._hash(key)
                self.slots[new_slot] = key
                self.data[new_slot] = value

    def _add(self, key, value):
        # None is being used for the empty slots and '' is being used for
        # dummy values so can't allow these as key.
        if key in (None, ''):
            raise Exception(F"Cannot hash {key} as key for hash table!!")
        slot_no = self._hash(key)
        self.length += 1
        if self.slots[slot_no] is None:
            self.slots[slot_no] = key
            self.data[slot_no] = value
        else:
            while self.slots[slot_no] not in (None, "", key):
                slot_no = self._increment(slot_no)
            if self.slots[slot_no] == key:
                print("key found updating: ", key)
                # we're updating key so no need to increase length
                self.length -= 1
            self.slots[slot_no] = key
            self.data[slot_no] = value

        if self.length / self.size >= self.max_load_factor:
            self._resize()

    def _get(self, key):
        slot_no = self._hash(key)
        if self.slots[slot_no] is None:
            raise Exception(F"Key: {key} not found!!")
        else:
            while self.slots[slot_no] not in (key, None):
                slot_no = self._increment(slot_no)
            if self.slots[slot_no] == key:
                return self.data[slot_no]
            else:
                raise Exception(F"Key: {key} not found!!")

    def _remove(self, key):
        slot_no = self._hash(key)
        if self.slots[slot_no] is None:
            raise Exception(F"Key: {key} not found!!")
        else:
            while self.slots[slot_no] not in (key, None):
                slot_no = self._increment(slot_no)
            if self.slots[slot_no] == key:
                self.slots[slot_no] = ""
                self.data[slot_no] = None
                self.length -= 1
            else:
                raise Exception(F"Key: {key} not found!!")

    def exists(self, key):
        slot_no = self._hash(key)
        if self.slots[slot_no] is None:
            exists = False
        else:
            while self.slots[slot_no] not in (key, None):
                slot_no = self._increment(slot_no)
            if self.slots[slot_no] == key:
                exists = True
            else:
                exists = False
        return exists


if __name__ == "__main__":
    h_table = HashTable()
    h_table["abc"] = 1
    h_table[1] = "abc"
    print(h_table)
    print("len:", len(h_table))
    h_table["32"] = "a"
    h_table["b"] = "abc"
    h_table["c"] = "d"
    print(h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))
    h_table["d"] = "g"
    print(h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))
    h_table[1] = "new 1 value"
    h_table["abc"] = "new abc value"
    h_table["32"] = "new 32 value"
    h_table["b"] = "new b value"
    h_table["c"] = "new c value"
    h_table["d"] = "new d value"

    print("<==== After update ====>")
    print(h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))
    h_table["e"] = 1
    h_table["f"] = 2
    h_table["g"] = 3
    h_table["h"] = 4
    print(h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))
    h_table[(1, 2)] = "tuple value"
    print(h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))

    print("abc exists: ", h_table.exists("abc"))
    print("dbc exists: ", h_table.exists("dbc"))

    print("===> Delete test <===")
    del h_table["abc"]
    del h_table[1]
    try:
        del h_table["dbc"]
    except Exception as e:
        print(e)
    print("after removing 1 and abc:", h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))
    print("slots:", h_table.slots)
    h_table["abc"] = 'resurrected'
    h_table[1] = 'resurrected'
    print("After adding again:", h_table)
    print("size:", h_table.size)
    print("len:", len(h_table))
    print("slots:", h_table.slots)

    print("===> Invalid Insertion <===")
    try:
        h_table[""] = "ankit"
    except Exception as e:
        print(e)
    try:
        h_table[None] = "sagar"
    except Exception as e:
        print(e)
    try:
        h_table[["a", "b", "c"]] = "sagar"
    except Exception as e:
        print(e)
