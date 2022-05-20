# Program ini meminta pengguna memasukkan sebuah nama kota
# dan menambahkan nama kota yang dimasukkan tersebut ke file kota.txt
def main():
    
    # [1] Tuliskan staement untuk meminta nama kota ke pengguna dengan prompt: "Masukkan nama kota: "
    kota = input("Masukkan nama kota: ")

    
    # [2] Tuliskan statement untuk membuka file kota.txt untuk ditulis dengan modus 'a' dan referensikan object file ke variabel output_file
    var = open('kota.txt','a')

    
    # [3] Tuliskan statement untuk menulis nama kota yang dimasukkan pengguna dalam baris baru
    var.write(kota)

    
    # [4] Tuliskan statement untuk menutup file
    var.close()

    
    # [5] Tuliskan statement yang menampilkan pesan "Data telah ditambahkan ke file kota.txt."
    print("Data telah ditambahkan ke file kota.txt.")

    
# Panggil fungsi main
main()
