def main():
    while(True):
        angka1 = int(input("Masukkan angka 1: "))
        angka2 = int(input("Masukkan angka 2: "))
        print("Jumlah =",angka1+angka2)
        trus = input("Masukkan y untuk melanjutkan: ")
        if (trus != 'y'): break
    
main()
