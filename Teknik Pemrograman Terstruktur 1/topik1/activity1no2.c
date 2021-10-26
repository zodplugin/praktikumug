// Program perhitungan penjumlahan angka1 dan angka2
#include <stdio.h>

// Fungsi main untuk memulai eksekusi program
int main()
{
    printf( "Masukkan 2 angka untuk dihitung: " ); // Mencetak output kalimat

    // Deklarasi variabel angka1 dan angka2
    int angka1,angka2; 
    
    // Deklarasi variabel penjumlahan dan pengurangan
    int penjumlahan,pengurangan ;
    
    scanf( "%d%d", &angka1, &angka2); // Membaca input variabel angka1 dan angka2
    
    // Menghitung nilai penjumlahan dan pengurangan dari variabel angka1 dan angka2
    penjumlahan = angka1 + angka2 ;
    pengurangan = angka1 - angka2 ;
    
    // Cetak output dengan memanggil variabel
    printf( "Hasil penjumlahan 2 bilangan: %d\n",penjumlahan ); // Menampilkan hasil penjumlahan
    printf( "Hasil pengurangan 2 bilangan: %d",pengurangan ); // Menampilkan hasil pengurangan
    
    return 0; // Menentukan nilai balik
} // Mengakhiri fungsi main()
