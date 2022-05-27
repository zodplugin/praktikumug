# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # Variabel sebagai penanda jika nama mahasiswa yang dicari ditemukan
    found = False
    
    try:
        # [1] Tuliskan statement untuk meminta nama file ke pengguna
        # Gunakan prompt: 'Masukkan nama file: '
        inputfile = input("Masukkan nama file: ")

        # [2] Tuliskan staement untuk membuka file dengan nama file yang diberikan pengguna
        # Anda dapat menggunakan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
        with open(inputfile, 'r') as myfile :
            print(f"File {inputfile} berhasil dibuka.\n")
            # [3] Tampilkan pesan: "File <nama_file> berhasil dibuka.". Tambahkan baris baru.
            namamhs = input("Masukkan nama mahasiswa yang ingin dicari: ")
            
            # [4] Tuliskan statement untuk meminta nama mahasiswa yang ingin dicari
            # Gunakan prompt: 'Masukkan nama mahasiswa yang ingin dicari: '
            nama = myfile.readline()
            while nama != '':
                nilai = myfile.readline()
                nama = nama.rstrip('\n')
                nilai = nilai.rstrip('\n')
                
                
                if (nama == namamhs):
                    print(f"Nama Mahasiswa: {nama}")
                    print(f"Nilai: {nilai}")
                    found = True
                    
                    
            # [5] Tuliskan statement untuk membaca baris pertama dari file (nama mahasiswa).
            # [6] Tuliskan loop while yang mengiterasi baris-baris file 
            
                # [7] Tuliskan statement untuk membaca nilai mahasiswa
                
                

                # [8] Tuliskan statement untuk menghilangkan baris baru pada nama mahasiswa dan nilai mahasiswa
                # Gunakan rstrip.
                
                
                # [9] Tuliskan struktur seleksi yang menentukan apakah nama mahasiswa cocok
                # dengan nama yang ingin dicari
                
                    # [10] Jika nama_mahasiswa sama dengan nama yang ingin dicari
                    # Tampilkan Nama dan Nilai
                    

                    # [11] Tetapkan nilai variabel penanda found dengan True
                    # Ini karena mahasiswa ditemukan
                    

                # [12] Tuliskan statement membaca baris berikutnya
                nama = myfile.readline()

    # [13] Tuliskan klausa except FileNotFoundError
    # Pada body klausa except ini tampilkan: File <nama_file> tidak ditemukan.
    except FileNotFoundError:
        print(f"File {inputfile} tidak ditemukan.")
        
    # [14] Tuliskan klausa else
    # Pada body klausa else tuliskan struktur seleksi jika found tidak sama dengan True
    # tampilkan pesan: "Nama <nama yang dicari> tidak ditemukan."
    else :
        if found != True:
            print(f"Nama {namamhs} tidak ditemukan.")
        
                    
# Panggil fungsi main
main()
