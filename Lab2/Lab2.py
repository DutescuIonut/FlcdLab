

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def toString(self):
        elements = []
        for index in range(self.capacity):
            current = self.table[index]
            while current:
                elements.append(f"{current.key}: {current.value}")
                current = current.next

        return elements
    
    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        # BC: O(1) - when near zero collisions, the linked list is always of len1
        # WC : O(n) - have to search if the key already exists in order to update the value, then update/ add new node
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        # BC: O(1) - the element is the head of the list
        # WC: O(n) - have to parse the whole linked list to find the element
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return -2

    def getPositionPair(self, key):
        # BC: O(1) - the element is the head of the list
        # WC: O(n) - have to parse the whole linked list to find the element
        index = self._hash(key)
        current = self.table[index]
        columnIndex = -1
        while current:
            columnIndex += 1
            if current.key == key:
                return (index,columnIndex)
            current = current.next

        return -2

    def remove(self, key):
        # BC: O(1) - the element is the head of the list
        # WC: O(n) - have to parse the whole linked list to find the element
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        # O(1)
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def getValueIndex(self, elem):
        index = self._hash(elem)

        if self.table[index] is not None:
            current = self.table[index]
            position = 0

            while current:
                if current.key == elem:
                    return (index, position)
                current = current.next
                position += 1

        return None


class ConstantsSymbolTable(HashTable):
    # Has HashTable's time complexities
    def insert(self, key, value):
        super().insert(key, value)

    def contains(self, key):
        try:
            super().search(key)
            return True
        except KeyError:
            return False

    def getValueIndex(self, key):
        return super().getValueIndex(key)

    def remove(self, key):
        super().remove(key)
        
    def toString(self):
        return super(ConstantsSymbolTable, self).toString()


class IdentifiersSymbolTable(HashTable):
    # Has HashTable's time complexities
    def insert(self, key, value):
        super().insert(key, value)

    def contains(self, key):
        try:
            super().search(key)
            return True
        except KeyError:
            return False

    def getValueIndex(self, key):
        return super().getValueIndex(key)

    def remove(self, key):
        super().remove(key)
    
    def toString(self):
       return super(IdentifiersSymbolTable, self).toString()

# Average time complexity is O(1) for all operations assuming there is a good hashing function
# that minimizes collisions as much as possible.
# The symbol tables are implemented as hash tables with chaining, meaning that
# for every hashed index of the table, we have a linked list that contains all the
# values that had a collision for that index.
# The linked list is implemented with Node class that has a value field, a key field and
# a next field that points to the next node in the linked list.
# The IdentifiersSymbolTable and ConstantsSymbolTable simply inherit the HashTable function
# and call all the methods from the super class.

