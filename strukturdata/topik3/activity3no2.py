# Implementasi ADT SortedLinkedList
class SortedLinkedList:
    # Constructor SortedLinkedList (dimulai dengan linked list kosong)
    def __init__(self):
        self._head = None
        self._size = 0

    # Method length() mengembalikan banyaknya elemen dalam sorted linked list.
    # Method ini diakses menggunakan fungsi len().
    def __len__(self):
        # Implementasikan method __len__ di bawah.
        return self._size


    # Method add(data) menambahkan data baru ke sorted linked list.
    def add(self, data):
        # Tuliskan implementasi method addLast(data) Anda di bawah.
        preNode = None
        curNode = self._head

        while curNode is not None and curNode.data < data:
            preNode = curNode
            curNode = curNode.next

        newNode = _Node(data)

        if curNode is self._head:
            newNode.next = self._head
            self._head = newNode
        else:
            newNode.next = preNode.next
            preNode.next = newNode

        self._size += 1

    # Method contains(data) digunakan untuk mencari data dalam sorted linked list.
    # Method ini diakses menggunakan operator in dan 
    # mengembalikan nilai Boolean: True jika data ditemukan dan False jika
    # data tidak ditemukan. 
    def __contains__(self, data):
        # Implementasikan method __contains__ di bawah.
        curNode = self._head
        found = False
        while curNode is not None and curNode.data != data:
            curNode = curNode.next
        if curNode is not None:
            found = True
        else:
            found = False
        return found
        
        
    # Method remove() menghapus data dari sorted linked list.
    # Method ini mengembalikan data yang dihapus.
    def remove(self, data):
        # Implementasikan method remove di bawah.
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
        
    # Method iterator untuk men-traverse sorted linked list
    # Method ini mengembalikan object dari class `_LinkedListIterator` 
    # dengan argumen referensi head.
    def __iter__(self):
        # Implementasikan method __iter__ di bawah
         return _LinkedListIterator(self._head)


# Definisikan class _Node sebagai penyimpanan data dan referensi 
# ke node selanjutnya.
class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class iterator untuk ADT Sorted Linked List
class _LinkedListIterator:
    # Implementasikan class _LinkedListIterator di bawah.
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
    
    
    
    
