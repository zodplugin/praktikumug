pembelian = int(input("Masukkan total pembelian: "))
print(f"Total Pembelian: Rp {pembelian:,.2f}")
ppn = 10/100 * pembelian
print(f"PPN (10%): Rp {ppn:,.2f}")
sc = 5/100 * pembelian
print(f"Service Charge (5%): Rp {sc:,.2f}")
total = pembelian + sc + ppn
print(f"Total yang harus dibayarkan: Rp {total:,.2f}")
