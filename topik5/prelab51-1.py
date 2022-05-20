# Program ini menuliskan teks "Bandung", "Jakarta", "Depok" masing-masing dalam satu baris ke file kota.txt
def main():
    # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dan referensikan object file ke variabel output_file
    output_file = open('kota.txt', 'w')

    
    # [2] Tuliskan statement-statement untuk menulis teks 'Bandung', 'Jakarta', 'Depok' 
    # masing-masing dalam satu baris ke file kota.txt denga method write.
    output_file.write('Bandung\nJakarta\nDepok')


    
    # [3] Tuliskan statement untuk menutup file kota.txt
    output_file.close()

    
# Panggil fungsi main
main()
