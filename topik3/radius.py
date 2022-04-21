import math

radius = float(input("Masukkan radius lingkaran (cm): "))
l = math.pi * radius * radius
k = 2 * math.pi * radius
print(f"Luas lingkaran dengan radius {radius:.2f} =  {l:.2f} cm2")
print(f"Keliling lingkaran dengan radius {radius:.2f} = {k:.2f} cm")
