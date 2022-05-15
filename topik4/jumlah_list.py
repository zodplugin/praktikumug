def jumlah_list(input_list):
    # Tuliskan kode Anda di bawah.
    # [1] Buat dua variabel akumulator untuk menyimpan jumlah elemen-elemen genap dan jumlah elemen-elemen ganjil
    ganjil = 0
    genap = 0
    
    # [2] Gunakan struktur loop untuk mengiterasi indeks dari input_list
    # Gunakan juga struktur seleksi dengan modulus untuk menguji indeks genap dan ganjil dan akumulasikan
    # elemen dengan indeks tersebut ke variabel akumulator yang sesuai
    for i in range(len(input_list)):
       if i%2 == 0 :
           genap += input_list[i]
       else :
           ganjil += input_list[i]
    print("Total elemen indeks ganjil: ",(ganjil))
    print("Total elemen indeks genap: ",(genap))
    # [3] Tampilkan jumlah elemen-elemen tersebut dengan teks:
    # "Total elemen indeks ganjil: <total_ganjil>"
    # "Total elemen indeks genap: <total_genap>"
