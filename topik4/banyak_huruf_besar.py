# Fungsi ini menghitung banyaknya huruf besar dari argumen yang diberikan dan mengembalikan
# jumlah huruf besar.
def banyak_huruf_besar(input_string):
    
    # [1] Buat sebuah variabel penghitung yang digunakan untuk menghitung banyak_huruf_besar dan inisialisasi dengan 0
    banyak_hurup = 0
    
    # [2] Tuliskan loop yang mengiterasi karakter-karakter dalam input_string dan uji apakah karakter tersebut adalah huruf besar
    # dengan method isupper(). Jika ya, inkrementasi variabel penghitung.
    for i in input_string:
        if i.isupper():
            banyak_hurup+=1
    
    # [3] Kembalikan variabel penghitung
    return banyak_hurup
