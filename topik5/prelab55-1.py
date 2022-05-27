# Program ini menambahkan record nilai mahasiswa
# ke file nilai_mahasiswa.txt
def main():
    # [1] Minta pengguna berapa banyak record yang ingin dimasukkan
    banyak = int(input("Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? "))
    
    # [2] Buka file dengan statement with, minta input masing-masing record ke pengguna, dan tulis ke file
    # nilai_mahasiswa.txt
    with open('nilai_mahasiswa.txt','a') as myfile:
        for i in range(1, banyak + 1):
            print(f'Masukkan record nilai mahasiswa ke {i}')
            nama = input('Nama: ')
            nilai = input('Nilai: ')
            print()
            
            myfile.write(nama + '\n')
            myfile.write(nilai + '\n')





# Panggil fungsi main
main()
