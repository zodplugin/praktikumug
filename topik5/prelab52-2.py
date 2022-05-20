# Program ini membaca isi file angka_float.txt
# dan mengalikan angka yang terdapat dalam file tersebut
def main():
    
    # [1] Buka file dengan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
    # Lalu ambil angka pertama pada baris pertama dan angka kedua pada baris kedua, simpan
    # angka pada setiap baris isi file masing-masing ke sebuah variabel 
    with open('angka_float.txt','r') as var:
        angka1 = var.readline().rstrip('\n')
        angka2 = var.readline().rstrip('\n')

        
    # [2] Hitung hasi kali dan tampikan sesuai dengan ketentuan program yang diminta
    result = float(angka1)*float(angka2)
    print("Baris 1 file angka_float.txt berisi:",angka1)
    print("Baris 2 file angka_float.txt berisi:",angka2)
    print(f"Hasil kali baris 1 dan baris 2 = {result:.2f}")





# Panggil fungsi main
main()
