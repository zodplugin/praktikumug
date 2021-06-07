import math


def luas(alas,tinggi):
    luas = 1/2 * alas * tinggi
    return luas
def keliling(alas,tinggi):
    sisimiring = math.sqrt(alas**2 + tinggi**2)
    keliling = alas + tinggi + sisimiring
    return keliling