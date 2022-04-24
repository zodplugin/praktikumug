# Fungsi konversi_ke_km
# [1] Tambahkan parameter yang diperlukan
def konversi_ke_km(Mil):
    # [2] Konversi argumen ke km dan kembalikan hasilnya.
    Km=Mil*1.6
    return Km

# Fungsi main
def main():
    # [3] Minta pengguna memasukkan jarak dalam mil dalam tipe floating point
    mil = float(input('Masukkan jarak dalam mil: '))

    # [4] Panggil fungsi konversi_ke_km
    konversi_ke_km(mil)
    
    # [5] Tampilkan hasil konversi
    print(f"Jarak dalam km = {konversi_ke_km(mil):.2f}")
    
main()
