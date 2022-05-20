# Program ini membaca file kota.txt dan menampilkan isi file
# dengan format: Baris <n>: <isi_file_baris_ke_n>
def main():
    
    # [1] Tuliskan statement untuk membuka file kota.txt untuk dibaca dan tugaskan object file ke sebuah variabel
    with open('kota.txt','r') as var:
        

    
    # [2] Tuliskan tiga statement untuk membaca tiga baris dari file kota.txt dan menyimpan isinya ke sebuah variabel
        baris1 = var.readline().rstrip('\n')
        baris2 = var.readline().rstrip('\n')
        baris3 = var.readline().rstrip('\n')



    
    # [4] Hilangkan karakter baris baru pada masing-masing isi baris





    # [3] Tampikan isi per baris dengan format: Baris <n>: <isi_file_baris_ke_n>
    print(f"Baris 1: {baris1}")
    print(f"Baris 2: {baris2}")
    print(f"Baris 3: {baris3}")



# Panggil fungsi main
main()
