# Program ini menambahkan teks 'Surabaya' dan 'Medan'
# masing-masing dalam satu baris ke file kota.txt
def main():
    # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dengan modus 'a'
    myfile = open('kota.txt','a')


    # [2] Tuliskan statement untuk menambahkan teks 'Surabaya' dan 'Medan' ke file kota.txt
    myfile.write("Surabaya\nMedan")


    
    # [3] Tuliskan statement untuk menutup file kota.txt
    myfile.close()


# Panggil fungsi main
main()
