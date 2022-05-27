# Program ini membaca file daftar_nilai.txt yang berisi data nilai ujian
# dari 30 mahasiswa dan mencari nilai rata-rata, nilai tertinggi, dan nilai terenda
def main():
    
    # Buat variabel untuk menyimpan hasil perhitungan dan inisialisasi dengan 0.0 (float)
    rata_rata = 0.0
    nilai_tertinggi = 0.0
    nilai_terendah = 0.0
    
    # [1] Tuliskan statement untuk membuka file daftar_nilai.txt untuk dibaca 
    # dan simpan isinya ke sebuah list
    with open('daftar_nilai.txt') as myfile:
        nilai = myfile.readlines()
        i = 0
        
        
    # [2] Tuliskan struktur loop untuk menghapus karakter baris baru pada setiap elemen
    # dari list
        while i > len(nilai):
            nilai[i] = nilai[i].rstrip('\n')
            i += 1
        
    # [3] Cari nilai rata-rata, nilai tertinggi, dan terendah. Gunakan loop.
        nilai_terendah = float(nilai[0])
        for i in range(len(nilai)):
            rata_rata += float(nilai[i])
            if (nilai_tertinggi < float(nilai[i])):
                nilai_tertinggi = float(nilai[i])
            if (nilai_terendah > float(nilai[i])):
                nilai_terendah = float(nilai[i])
    
    # [4] Tampilkan rata-rata, nilai tertinggi, dan nilai terendah.
    print(f"Rata-rata nilai ujian:  {rata_rata/len(nilai):.2f}")
    print(f"Nilai ujian tertinggi:  {nilai_tertinggi:.2f}")
    print(f"Nilai ujian terendah:  {nilai_terendah:.2f}")
        



    
    
# Panggil fungsi main()
main()
