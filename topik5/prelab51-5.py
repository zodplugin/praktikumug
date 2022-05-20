# Program ini membaca file menggunakan statement with
def main():

    # [1] Buka file kota.txt untuk dibaca dan tugaskan object file ke variabel input_file
    # dengan statement with. Lalu simpan seluruh isi file ke sebuah variabel bernama isi_file.
    with open("kota.txt",'r') as input_file:
        isi_file = input_file.read()
    



    # [2] Tampilkan isi file dengan print
    print(isi_file)



# Panggil fungsi main
main()
