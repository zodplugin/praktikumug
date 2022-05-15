def get_score():
    # Buat list kosong untuk menyimpan angka-angka yang dimasukkan pengguna
    score_list = []
    
    
    # [1] Minta penggunakan memasukkan skor berupa angka
    a = int(input("Masukkan skor (masukkan angka negatif untuk menyudahi): "))
    while a > -1 :
        score_list.append(a)
        a = int(input("Masukkan skor (masukkan angka negatif untuk menyudahi): "))

    # [2] Tulis struktur loop yang meminta pengguna memasukkan angka-angka


    return score_list
