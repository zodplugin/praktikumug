# Class Bag adalah implementasi dari ADT Bag
class Bag:
    def __init__(self):
        self._isi = list()

    def __len__(self):
        return len(self._isi)

    def __contains__(self, nilai):
        return nilai in self._isi

    def add(self, nilai):
        self._isi.append(nilai)

    def remove(self, nilai):
        if nilai not in self._isi:
            raise ValueError('Nilai tidak ada di bag.')
        else:
            index = self._isi.index(nilai)
            return self._isi.pop(index)

    # Method numOf(data) menerima sebuah argument berupa nilai data 
    # dan mengembalikan banyaknya kemunculan nilai data tersebut di dalam bag.
    def numOf(self, data):
        numofdata = 0 
        if data not in self._isi:
            return ('Nilai tidak ada di bag.')
        else :
            for i in self._isi:
                if i == data:
                    numofdata += 1
            return numofdata

    def __iter__(self):
        return _BagIterator(self._isi)

# Class _BagIterator adalah class iterator untuk membuat sebuah object
# dapat diiterasi.
class _BagIterator:

    def __init__(self, isi):
        self._isiBag = isi
        self._curIndeks = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._curIndeks < len(self._isiBag):
            item = self._isiBag[self._curIndeks]
            self._curIndeks += 1
            return item
        else:
            raise StopIteration
