def main():
    detik = int(input("Masukkan jumlah detik: "))
     # melakukan konversi hh:mm:ss ke detik
    hari = detik // 86400
    sisahari = detik % 86400
    jam = sisahari // 3600
    sisadetik = sisahari % 3600
    menit = sisadetik // 60
    detik = sisadetik % 60
    
    if jam == 0 and hari ==0:
        print(f"{menit} menit {detik} detik")
    elif (hari == 0):
        print(f"{jam} jam {menit} menit {detik} detik")
    else:
        print(f"{hari} hari {jam} jam {menit} menit {detik} detik")

main()
