# Program ini menuliskan sebuah list ke file list_angka.txt
def main():
    
    angka = [234, 694, 123, 789, 923, 674, 534]
    
    # [1] Tuliskan kode untuk menuliskan list yang direferensikan oleh variabel angka
    # ke file list_angka.txt
    with open('list_angka.txt','w') as myfiles:
        for i in angka:
            myfiles.write(str(i)+"\n")
    
# Panggil fungsi main
main()
