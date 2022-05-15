def main():
    # [1] Minta input ke pengguna
    a = int(input("Masukkan sebuah angka: "))
    # [2] Buat sebuah variabel akumulator
    
    total = 0
    
    # [3] Iterasi karakter-karakter (digit-digit) dalam string angka yang dimasukkan pengguna
    res = list(map(int, str(a)))
    for i in res:
        total += i
        
    # dan konversi ke integer untuk mendapatkan representasi integer dari digit
    print("Jumlah digit-digit dari "+str(a)+" =",total)
    # [4] Tampilkan jumlah digit dengan teks: "Jumlah digit-digit dari <input_angka_pengguna> = <jumlah_digit>"
    
# Panggil fungsi main
main()
