from array2d import Array2D


# Implementasi ADT Matriks
class Matriks:
    def __init__(self, bykBaris, bykKolom):
        self._arr2D = Array2D(bykBaris, bykKolom)
        self._arr2D.clear(0)

    def bykBaris(self):
        return self._arr2D.bykBaris()

    def bykKolom(self):
        return self._arr2D.bykKolom()

    def __getitem__(self, indexTuple):
        return self._arr2D[indexTuple[0], indexTuple[1]]

    def __setitem__(self, indexTuple, nilai):
        self._arr2D[indexTuple[0], indexTuple[1]] = nilai

    def kaliSkalar(self, skalar):
        for brs in range(self.bykBaris()):
            for klm in range(self.bykKolom):
                self[brs, klm] *= skalar

    def transpos(self):
        trMatrix = Matriks(self.bykKolom(), self.bykBaris())
        for brs in range(self.bykBaris()):
            for klm in range(self.bykKolom()):
                trMatrix[klm, brs] = self[brs, klm]
        return trMatrix

    def __add__(self, matriksLain):
        if (matriksLain.bykBaris() != self.bykBaris()) or \
                (matriksLain.bykKolom() != self.bykKolom()):
            raise ValueError('Matriks yang dijumlahkan harus berukuran sama.')
        else:
            hasil = Matriks(self.bykBaris(), self.bykKolom())
            for brs in range(self.bykBaris()):
                for klm in range(self.bykKolom()):
                    hasil[brs, klm] = self[brs, klm] + matriksLain[brs, klm]
            return hasil

    def __sub__(self, matriksLain):
        pass

    # Operasi multiply(matriksLain) mengembalikan matriks baru
    # hasil perkalian matriks ini dengan matriksLain.
    # Diakses menggunakan operator *.
    def __mul__(self, matriksLain):
        if (matriksLain.bykBaris() == self.bykBaris()) or \
                (matriksLain.bykKolom() == self.bykKolom()):
            raise ValueError('Matriks yang diberikan tidak sesuai!')
        else:
            hasil = Matriks(self.bykBaris(), matriksLain.bykKolom())

            for i in range(self.bykBaris()):
                for j in range(matriksLain.bykKolom()):
                    for k in range(self.bykKolom()):
                        hasil[i, j] += self[i, k] * matriksLain[k, j]

            return hasil








