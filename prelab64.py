# Fungsi sortir menerima argumen list dan
# mengembalikan list yang tersortir
def sortir(data):
    # [1] Tuliskan kode algoritma penyortiran di bawah
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        kecil = []
        besar = []
        for i in data[1:]:
            if i <= pivot:
                kecil.append(i)
            else:
                besar.append(i)
        return sortir(kecil) + [pivot] + sortir(besar)
        
    
# Fungsi median menerima argumen sebuah list
# dan mengembalikan nilai median dari data dalam list tersebut
def median(data):
    # [2] Gunakan fungsi sortir untuk menyortir data
    datamed = sortir(data)
    # [3] Hitung median dengan dua kondisi untuk jumlah data genap dan jumlah data ganjil
    # lalu kembalikan nilai median
    lenn = len(data)
    nilaiMedian = (lenn - 1) // 2
    
    if lenn % 2 == 1:
        return datamed[nilaiMedian]
    else:
        return (datamed[nilaiMedian] + datamed[nilaiMedian + 1]) / 2.0
        



#########################################################################

# Fungsi bantu untuk mencari indeks dari nilai minimum dalam data
# Fungsi ini mengembalikan indeks nilai minimum dari data
def indeks_minimum(data):
    # [1] Tuliskan kode untuk mencari indeks nilai minimum
    # dan kembalikan indeks tersebut.
    index_min = 0
    min = data[index_min]
    for i in range(1, len(data)):
        if data[i] <= min:
            index_min = i
            min = data[index_min]
    return index_min


# Fungsi penyortiran seleksi secara rekursif
def selection_sort_rekursif(data):
    data_tersortir = []
    # [2] Base Case: Data kosong atau hanya mempunyai satu elemen
    # Tidak perlu sortir, kembalikan data apa adanya
    if len(data) <= 1:
        return data
    else:
        indexmin = indeks_minimum(data)
        data_tersortir.append(data[indexmin])
        data.pop(indexmin)
        return selection_sort_rekursif(data_tersortir) + selection_sort_rekursif(data)



