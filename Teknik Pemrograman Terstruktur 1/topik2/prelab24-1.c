#include <stdio.h>

int main()
{
    // Mendeklarasikan variabel angka dengan tipe data int
    int angka;
    
    // Mencetak output kalimat dan input ke variabel angka
    printf("MENU MAKANAN \n");
    printf("1. Nasi + ayam + es teh manis \n");
    printf("2. Nasi + ayam + tempe + es teh manis \n");
    printf("3. Nasi + ayam + tempe tahu + es jeruk peras \n\n");
    printf("Masukkan nomor menu (1-3) = \n");
    scanf("%d",&angka);
    
    // Perulangan switch dengan dua buah case
    switch (angka)
    {
    case 1: // case akan dijalankan jika nomor yang di-input adalah 1
        printf("Menu 1: Nasi + ayam + es teh manis \n");
        printf("Harga: Rp. 20.000 \n");
        break;
    case 2: // case akan dijalankan jika nomor yang di-input adalah 2
        printf("Menu 2: Nasi + ayam + tempe + es teh manis \n");
        printf("Harga: Rp. 25.000 \n");
        break;
    case 3: // case akan dijalankan jika nomor yang di-input adalah 3
        printf("Menu 3: Nasi + ayam + tempe tahu + es jeruk peras \n");
        printf("Harga: Rp. 30.000 \n");
        break;    
    default: // default akan dijalankan jika nomor yang di-input selain 1 dan 2
        printf("Maaf format nomor menu tidak sesuai \n");
    } // Akhir switch
    
    return 0;
}
