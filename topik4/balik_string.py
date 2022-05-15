# Fungsi ini membalik urutan karakter-karakter dari input_string
# Fungsi ini tidak mengembalikan apapun namun menampilkan string dengan karakter-karakter kebalikan dari
# input_string
def balik_string(input_string):
    # [1] Buat sebuah variabel untuk menyimpan string dengan urutan karakter terbalik. Inisialisasi dengan string kosong.
    str = "" 
    for i in input_string: 
        str = i + str 
    print(str)
        
    
    # [2] Iterasi karakter-karakter dari input string dimulai dari indeks terakhir sampai dengan indeks pertama
    # Konkatenasi setiap karakter ke variabel yang menyimpan string dengan urutan karakter terbalik.

    
    # [3] Print variabel yang menyimpan string dengan urutan karakter terbalik.
