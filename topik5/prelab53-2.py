def main():
    
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah
    
    
    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    total = 0
    baris = 0
    
    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    myfile = open('sales.txt','r')
    
    
    
    isi = myfile.readline()
    while isi != '':
        isix = float(isi)
        total += isix
        baris += 1
        isi = myfile.readline()
        
    myfile.close()
    
    totalfix = total / baris
    print(f"Rata-rata penjualan: {totalfix:,.2f}")
    
    # [3] Baca baris pertama isi file dan simpan ke suatu variabel
    
    
    # [4] Tuliskan loop while untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
    # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
    # - inkrementasi variabel penghitung baris
    
    
    
    
    # [5] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.    
    



# Panggil fungsi main
main()
