
# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # [1] Buka file nilai_mahasiswa.txt dengan statement with untuk dibaca
    # Pada body statement with:
    # - Gunakan loop while untuk membaca field-field dari semua record
    # - Tampilkan record dengan tampilan:
    #           Nama: <nama_mahasiswa>
    #           Nilai: <nilai_mahasiswa>
    with open('nilai_mahasiswa.txt','r') as myfile:
        nama = myfile.readline()
        while nama != '':
            nilai = myfile.readline()
            
            nama = nama.rstrip('\n')
            nilai = nilai.rstrip('\n')
            
            
            print(f'Nama: {nama}')
            print(f'Nilai: {nilai}')
            print()
            
            nama = myfile.readline()
            
            
# Panggil fungsi main
main()
