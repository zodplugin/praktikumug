// Program perhitungan aritmatika
#include <stdio.h>

// Fungsi main untuk memulai eksekusi program
int main()
{
    printf( "Masukkan 3 angka: " ); // Mencetak kalimat

    // Deklarasi variabel x, y, dan z
    int x,y,z ; 
    
    // Deklarasi variabel perkalian, penjumlahan, dan pengurangan
    int perkalian,penjumlahan,pengurangan;
    
    scanf("%d\n%d\n%d", &x,&y,&z ); // Membaca input variabel x, y, dan z
    
    // Menghitung nilai perkalian, penjumlahan, dan pengurangan dari variabel x, y, dan z
    perkalian = x * y  * z; 
    penjumlahan = x + y + z ;
    pengurangan = x - y - z;
    
    // Cetak output dengan memanggil variabel
    printf( "Hasil penjumlahan 3 bilangan: %d\n", penjumlahan ); 
    printf( "Hasil perkalian 3 bilangan: %d\n", perkalian ); 
    printf( "Hasil pengurangan 3 bilangan: %d", pengurangan); 
    
    return 0 ; // Menentukan nilai balik
} // Mengakhiri fungsi main()
