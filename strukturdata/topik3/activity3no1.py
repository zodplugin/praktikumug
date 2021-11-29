# Implementasi ADT LinkedList
class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def addFirst(self, data):
        newNode = _Node(data)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    # Method addLast(data) menambahkan data ke akhir linked list.
    # Method ini tidak mengembalikan nilai.
    def addLast(self, data):
        # Tuliskan implementasi method addLast(data) Anda di bawah.
        if self._head is None:
            newNode = _Node(data)
            newNode.next = self._head
            self._head = newNode
            self._size += 1
        else :
            newNode = _Node(data)
            curNode = self._head
            while curNode.next :
                curNode = curNode.next
            curNode.next = newNode
            self._size += 1
        
    def __contains__(self, data):
        curNode = self._head
        found = False
        while curNode is not None and curNode.data != data:
            curNode = curNode.next
        if curNode is not None:
            found = True
        else:
            found = False
        return found

    def remove(self, data):
        curNode = self._head
        prevNode = None
        while curNode is not None and curNode.data != data:
            prevNode = curNode
            curNode = curNode.next
        if curNode is None:
            raise ValueError('Data tidak ditemukan.')
        else:
            self._size -= 1
            if curNode is self._head:
                self._head = curNode.next
            else:
                prevNode.next = curNode.next
        
        return curNode.data

    def __iter__(self):
        return _LinkedListIterator(self._head)

class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class _LinkedListIterator:
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            data = self._curNode.data
            self._curNode = self._curNode.next
            return data
