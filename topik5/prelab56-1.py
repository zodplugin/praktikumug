# Program ini meminta pengguna memasukkan dua angka untuk operasi pembagian
# Program menampilkan pesan jika terjadi eksepsi
def main():
    # [1] Tuliskan statement try/except
    # Pada body klausa try:
    #     - Minta dua angka ke pengguna
    #     - Lakukan pembagian
    # Pada body klausa except untuk ValueError
    #     - Tampilkan pesan: "Nilai yang diinput salah."
    # Pada body klausa except untuk ZeroDivisionError
    #     - Tampilkan pesan: "Tidak dapat membagi dengan nol."
    try:
        angka1 = int(input('Masukkan sebuah angka yang akan dibagi: '))
        angka2 = int(input('Masukkan sebuah angka pembagi: '))
        hasil = angka1 / angka2
    except ValueError:
        print("Nilai yang diinput salah.")
    except ZeroDivisionError:
        print("Tidak dapat membagi dengan nol.")
    else:
        print(f'{angka1} dibagi dengan {angka2} sama dengan {hasil:.1f}')


# Panggil fungsi main
main()
