def main():
    karakter_list = []
    # Variabel untuk menyimpan banyaknya karakter yang terdapat dalam string yang diinput pengguna
    banyak_karakter = []
    alfabet = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0,
               "v":0, "w":0, "x":0, "y":0, "z":0}
    total_huruf = 0
    alfabett = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # Catatan untuk dua variabel di atas:
    # Misalkan pengguna memasukkan 'ada', maka
    # karakter_list akan berisi ['a', 'd']
    # banyak_karakter akan berisi [2, 1]
    # Yang berarti terdapat 'a' sebanyak 2 dan terdapat 'd' sebanyak 1

    # [1] Minta pengguna masukkan sebuah teks dengan prompt 'Masukkan sebuah teks: ' dan simpan dalam sebuah variabel
    text = input("Masukkan sebuah teks: ")

    # [2] Gunakan method lower untuk konversi semua karakter ke huruf kecil. Karena string immutable, Anda harus menugaskan
    # kembali nilai kembali method ke variabel pada [1]
    text.islower()

    # [3] Gunakan struktur loop untuk mengterasi string input mulai dari indeks 0 sampai dengan terakhir.
    # Di dalam loop ini juga terdapat loop yang mengiterasi karakter_list dan menguji masing-masing karakter dalam karakter_list dengan
    # karakter dari input_string
    for i in text:
        if i in alfabett:
            alfabet[i] += 1


    if (text[0] == 'S') or (text[0] == 's'):
        alfabet["s"] += 1
        max_key = max(alfabet, key=alfabet.get)
        print("Karakter terbanyak:  s")
    else :
        max_key = max(alfabet, key=alfabet.get)
        print("Karakter terbanyak: ",max_key)


    


    # [4] Cari jumlah terbanyak pada banyak_karakter dan simpan indeksnya



    # [5] Tampilkan karakter terbanyak. Gunakan indeks yang didapat pada [4]        


# Panggil fungsi main
main()
