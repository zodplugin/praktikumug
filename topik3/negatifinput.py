# Program ini menghitung rata-rata dari rangkaian input yang dimasukkan pengguna
def main():
    total = 0
    range = 0
    pos = int(input("Masukkan angka positif (akhiri dengan memasukkan angka negatif): "))
    while pos >= 0 : 
        total += pos
        range += 1
        pos = int(input("Masukkan angka positif (akhiri dengan memasukkan angka negatif): "))
        
    
    if total <= 0:
        rata = 0
        print(f"Rata-rata angka yang dimasukkan: {rata}")
    else:
        rata = total / range
        print(f"Rata-rata angka yang dimasukkan: {rata}")


# Panggil fungsi main
main()
