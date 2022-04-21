def main():
    arr = []
    for i in range(1,3+1):
        arr.append(int(input(f"Masukkan angka {i}: ")))
    
    maxx = max(arr)
    print(f"Angka terbesar =  {maxx}")

main()
