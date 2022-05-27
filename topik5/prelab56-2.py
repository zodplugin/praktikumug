def main():
    # List untuk menyimpan isi file
    list_angka = []
    
    # [1] Tuliskan statement yang meminta pengguna memasukkan nama file dengan prompt: Masukkan nama file: "
    namafile = input("Masukkan nama file: ")
    # [2] Tuliskan exception handler dengan statement try/except
    # Pada body klausa try: buka file, baca isinya, dan simpan isinya ke list_angka
    # Pada body klausa except untuk FileNoFoundError tampilkan pesan "File tidak ditemukan."
    # Pada body klausa except untuk ValueError tampilkan pesan "Terdapat data non numerik dalam file."
    # Pada body klausa else: Cari rata-rata, nilai tertinggi, nilai terenda dan tampilkan hasilnya
    try:
        with open(namafile,'r') as myfile:
            for line in myfile:
                list_angka.append(float(line))
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except ValueError:
        print("Terdapat data non numerik dalam file.")
    else:
        bagi = 0
        total = 0
        nilai_terendah = list_angka[0]
        nilai_tertinggi = 0
        for i in list_angka:
            bagi += 1
            total += i
            if nilai_tertinggi < i:
                nilai_tertinggi = i
            if nilai_terendah > i :
                nilai_terendah = i
        rata_rata = total / bagi
        print(f"Rata-rata nilai: {rata_rata:.2f}")
        print(f"Nilai tertinggi: {nilai_tertinggi:.2f}")
        print(f"Nilai terendah: {nilai_terendah:.2f}")
        
# Panggil fungsi main
main()
