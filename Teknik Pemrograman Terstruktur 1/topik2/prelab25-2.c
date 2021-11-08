#include <stdio.h>

int main()
{
    // Mendeklarasikan variabel operator dengan tipe data int
    int oprAritmatika;
    
    // Mencetak output kalimat dan input ke variabel angka
    printf("Operator Aritmatika \n");
    printf("1. Penjumahan \n");
    printf("2. Pengurangan \n");
    printf("3. Perkalian \n");
    printf("4. Pembagian \n\n");
    printf("Masukkan nomor menu (1-4) = \n");
    scanf("%d",&oprAritmatika);
    
    // Perulangan switch dengan empat buah case
    switch (oprAritmatika)
    {
    case 1 : // case akan dijalankan jika nomor yang di-input adalah 1
        printf("Contoh penggunaan operator penjumalahan \n");
        printf("x = 1 + 2; \n");
        break;
    case 2 :// case akan dijalankan jika nomor yang di-input adalah 2
        printf("Contoh penggunaan operator pengurangan \n");
        printf("x = 1 - 2; \n");
        break;
    case 3 : // case akan dijalankan jika nomor yang di-input adalah 3
        printf("Contoh penggunaan operator perkalian \n");
        printf("x = 1 * 2; \n");
        break;  
    case 4 :  // case akan dijalankan jika nomor yang di-input adalah 3
        printf("Contoh penggunaan operator pembagian \n");
        printf("x = 1 / 2; \n");
        break;  
    default :  // default akan dijalankan jika nomor yang di-input selain 1, 2, 3, 4, dan 5
        printf("Maaf format nomor menu tidak sesuai \n");
    } // Akhir switch
    
    return 0;
}
