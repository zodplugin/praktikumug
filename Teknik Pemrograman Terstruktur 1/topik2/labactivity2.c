#include <stdio.h>

int main()
{
    // Mendeklarasikan variabel angka dengan tipe data int
    int angka;
    
    // Mencetak output kalimat dan input ke variabel angka
    printf("Masukkan nomor menu (1-2) = \n");
    scanf("%d", &angka );
    
    // Perulangan switch dengan parameter variabel angka
    switch (angka)
    {
    case 1 : // case akan dijalankan jika nomor yang di-input adalah 1
        printf("Menu 1: Nasi + ayam + tempe + es teh manis \n");
        printf("Harga: Rp. 25.000 \n");
        break;
    case 2 :  // case akan dijalankan jika nomor yang di-input adalah 2
        printf("Menu 2: Nasi + ayam + es teh manis \n");
        printf("Harga: Rp. 20.000 \n");
        break;
    case 3 :  // default akan dijalankan jika nomor yang di-input selain 1 dan 2
        printf("Maaf format nomor menu tidak sesuai \n");
    } // Akhir switch
    
    return 0;
}
