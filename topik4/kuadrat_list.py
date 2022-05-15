# Fungsi ini menerima sebuah list dan mengembalikan
# list baru yang elemen-elemennya adalah nilai kuadrat dari elemen-elemen list argumen
def kuadrat_list(input_list):
    # Tuliskan kode Anda di bawah.
    # List kosong untuk list yang dikembalikan
    output_list = []
    
    # [1] Tuliskan struktur loop yang mengiterasi input_list dan menambahkan elemen yang telah dikuadratkan ke output_list
    # Gunakan method append untuk menambahkan elemen ke list
    for i in range(len(input_list)):
        output_list.append(input_list[i]**2)
    
    # Kembalikan sebuah list yang elemen-elemennya adalah kuadrat dari elemen-elemen input_list
    return output_list
    
