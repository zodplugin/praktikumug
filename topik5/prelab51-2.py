# Program ini membaca keseluruhan isi file kota.txt
def main():
    # Tuliskan kode Anda di bawah.
    # [1] Tuliskan statement buka file kota.txt untuk dibaca
    file = open('kota.txt','r')


    # [2] Tuliskan statement untuk membaca keseluruhan isi file kota.txt dan simpan isi file dalam variabel isi_file
    isi_file = file.read()



    # [3] Tuliskan statement untuk menutup file kota.txt
    file.close()



    # [4] Tuliskan statement untuk mencetak nilai dari variabel isi_file yang menyimpan isi file kota.txt
    print(isi_file)


    
# Panggil fungsi main
main()
