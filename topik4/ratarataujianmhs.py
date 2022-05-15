# Program ini memroses nilai tiga ujian dari mahasiswa dalam sebuah kelas
# Program meminta pengguna memasukkan jumlah mahasiswa, meminta pengguna memasukkan
# nilai-nilai tiga ujian setiap mahasiswa, dan menampilkan rata-rata dari tiga nilai ujian dari setiap mahasiswa 
def main():
    
    # Variabel JUMLAH_UJIAN
    JUMLAH_UJIAN = 3
    # Variabel untuk menyimpan nilai-nilai ujian
    nilai_ujian = []
    
    # Tuliskan kode Anda di bawah
    # [1] Minta pengguna memasukkan jumlah mahasiswa 
    panjang = int(input("Masukkan jumlah mahasiswa: "))

    # [2] Gunakan nested loop untuk meminta pengguna memasukkan tiga nilai ujian dari masing-masing mahasiswa
    for i in range(panjang):
        tempnilai = 0
        print("==================================================")
        print(f"Masukkan nilai ujian untuk mahasiswa {i+1}")
        print("--------------------------------------------------")
        for x in range(JUMLAH_UJIAN):
            ujian = float(input(f"Masukkan nilai ujian ke-{x+1}: "))
            tempnilai += ujian
        nilai_ujian.append(tempnilai)
            
    print("==================================================")
    # [3] Gunakan nested loop untuk menghitung dan menampilkan rata-rata nilai ujian
    for i in range(len(nilai_ujian)):
        print(f"Rata-rata ujian mahasiswa {i+1}: {nilai_ujian[i]/JUMLAH_UJIAN:.2f}")



# Panggil fungsi main
main()
