import math

# Fungsi luas_lingkaran
def luas_lingkaran(radius):
    l = math.pi * radius * radius
    return l
    
# Fungsi keliling_lingkaran():
def keliling_lingkaran(radius):
    k = 2 * math.pi * radius
    return k

# Fungsi main
def main():
    radius = float(input("Masukkan radius lingkaran (cm): "))
    print(f"Luas lingkaran dengan radius {radius:.2f} =  {luas_lingkaran(radius):.2f} cm2")
    print(f"Keliling lingkaran dengan radius {radius:.2f} = {keliling_lingkaran(radius):.2f} cm")
    
# Panggil fungsi main
main()
    
