detik = int(input("Masukkan waktu dalam detik: "))
 # melakukan konversi hh:mm:ss ke detik
jam = detik // 3600
sisadetik = detik % 3600
menit = sisadetik // 60
detik = sisadetik % 60
print("Berikut waktu dalam jam, menit, dan detik:")
print(f"Jam: {jam}")
print(f"Menit: {menit}")
print(f"Detik: {detik}")
