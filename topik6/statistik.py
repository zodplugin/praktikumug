import math


def mean(data):
    bagi = 0
    total = 0
    for i in data:
        total += i
        bagi += 1
    mean = total / bagi
    return mean

def var(data):
    bagi = 0
    total = 0
    variasi = 0
    for i in data:
        total += i
        bagi += 1
    x = total / bagi
    for i in data:
        variasi += (i - x)**2
    result = variasi / bagi
    return  result

def std(data):
    bagi = 0
    total = 0
    variasi = 0
    for i in data:
        total += i
        bagi += 1
    x = total / bagi
    for i in data:
        variasi += (i - x)**2
    resultvariasi = variasi / bagi
    result = math.sqrt(resultvariasi)
    return result
def sortir(data):
    # [1] Tuliskan kode algoritma penyortiran di bawah
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        kecil = []
        besar = []
        for i in data[1:]:
            if i <= pivot:
                kecil.append(i)
            else:
                besar.append(i)
        return sortir(kecil) + [pivot] + sortir(besar)

def median(data):
    datamed = sortir(data)
    lenn = len(data)
    nilaiMedian = (lenn - 1) // 2

    if lenn % 2 == 1:
        return datamed[nilaiMedian]
    else:
        return (datamed[nilaiMedian] + datamed[nilaiMedian + 1]) / 2.0

