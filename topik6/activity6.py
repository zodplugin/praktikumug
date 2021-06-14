# [1] Impor module statistik yang Anda upload
import statistik

# Fungsi main menggunakan module statistik
# dan menampilkan statistik dari data dalam sebuah file
def main():
    
    # [2] Minta user memasukkan nama file yang berisi data
    # dengan prompt: 'Masukkan nama file: '
    nama_file = input("Masukkan nama file: ")

    # [3] Struktur try/except untuk error file tidak ditemukan
    # dan file berisi data non numerik
    # Baca isi file dan gunakan fungsi-fungsi pada module yang Anda tulis
    # untuk mendapatkan nilai mean, variansi, standard deviasi, median dan modus.
    # Dan tampilkan nilai-nilai tersebut dengan presisi dua desimal.
    
    try :
        data = []
        with open(nama_file,'r') as myfile:
            for i in myfile:
                data.append(float(i))
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    except ValueError:
        print(f"File {nama_file} berisi data non-numerik.")
    else:
        mean = statistik.mean(data)
        variansi = statistik.var(data)
        stdvar = statistik.std(data)
        med = statistik.median(data)
        
        print(f"Mean dari data: {mean:.2f}")
        print(f"Variansi dari data: {variansi:.2f}")
        print(f"Standar Deviasi dari data: {stdvar:.2f}")
        print(f"Median dari data: {med:.2f}")
        
                
    








        
# Panggil fungsi main
main()