class BST:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, nilaiDicari):
        return self._bstSearch(self._root, nilaiDicari) is not None

    def _bstSearch(self, subtree, target):
        if subtree is None :
            return None 
        elif target < subtree.data: # Target berada di subtree kiri.
            return self._bstSearch(subtree.left, target)
        elif target > subtree.data: # Target berada di subtree kanan
            return self._bstSearch(subtree.right, target)
        else: 
            return subtree

    def min(self):
        nodeMinimum = self._bstMinimum(self._root)
        if nodeMinimum is None:
            return 0
        return nodeMinimum.data
        
    def _bstMinimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)
    
    #### Implementasikan method max ####
    # Implementasi ini mirip dengan implementasi method min.
    # Gunakan method bantu untuk mencari node dengan data terkecil. 
    
    def _bstMaximum(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bstMaximum(subtree.right)

    def max(self):
        nodeMaximum = self._bstMaximum(self._root)
        if nodeMaximum is None:
            return 0
        return nodeMaximum.data


    ###############################

    def add(self, data):
        # Cari terlebih dahulu data di dalam tree.
        node = self._bstSearch(self._root, data)
        # Jika terdapat data dalam tree kembalikan False.
        # Jika data tidak ada dalam tree, masukkan data ke tree dengan
        # memanggil method bantu _btsInsert.
        if node is not None:
            return False
        else:
            self._root = self._bstInsert(self._root, data)
            self._size += 1
            return True

    def _bstInsert(self, subtree, data):
        # Jika subtree kosong
        if subtree is None:
            subtree = _BSTNode(data)
        elif (data < subtree.data):
            subtree.left = self._bstInsert(subtree.left, data)
        elif (data > subtree.data):
            subtree.right = self._bstInsert(subtree.right, data)
        return subtree

    def remove(self, dataDihapus):
        if dataDihapus not in self:
            raise Exception('Data tidak ada dalam tree.')
        else:
            self._root = self._bstRemove(self._root, dataDihapus)
            self._size -= 1

    def _bstRemove(self, subtree, target):
        # Cari target (data dari node yang ingin dihapus) dalam tree.
        if subtree is None:
            return subtree
        elif target < subtree.data:
            subtree.left = self._bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.data:
            subtree.right = self._bstRemove(subtree.right, target)
            return subtree
        # Node target ditemukan
        else:
            # Kasus 1: Node target adalah node leaf
            if subtree.left is None and subtree.right is None:
                return None
            # Kasus 2: Node target mempunyai satu child
            if subtree.left is None or subtree.right is None:
                # Kembalikan child dari node target yang dihapus
                # Jika descendant berada di child kiri, kembalikan child kiri.
                if subtree.left is not None:
                    return subtree.left
                # Jika descendant berada di child kanan, kembalikan child kanan.
                else:
                    return subtree.right
            # Kasus 3: Node target mempunyai dua child.
            else:
                successor = self._bstMinimum(subtree.right)
                subtree.data = successor.data
                subtree.right = self._bstRemove(subtree.right, successor.data)
                return subtree

# Class _BSTNode merepresentasikan node dalam binary search tree.
class _BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

