// Program maximum.c
#include <stdio.h>

// Fungsi prototype dengan nama fungsi maximum dan tiga parameter (x, y, z) bertipe data integer
int maximum(int x, int y, int z);

// Fungsi main untuk memulai eksekusi program
int main()
{
    // Deklarasikan tiga variabel bertipe data integer dengan nama variabel angka1, angka2, angka3
	int angka1, angka2, angka3;
    // Menginput tiga angka intger
    printf("%s", "Masukkan tiga angka: \n");
    scanf("%d%d%d", &angka1, &angka2, &angka3);
    // Mencetak output dengan memanggil fungsi maximum
     printf("Maximumnya adalah %d\n", maximum(angka1, angka2, angka3));
} // Mengakhiri fungsi main()

// Definisi fungsi maximum 
int maximum(int x, int y, int z)
{
    // Menugaskan variabel max untuk nilai x dengan tipe data integer
    int max = x;
    // Membuat statement if jika variabel y lebih besar dari max
    if ( y > max)
    {
    // Menugaskan variabel max dengan variabel y 
       max = y;	
    } 
// Membuat statement if jika z lebih besar dari variabel max
    if ( z > max)
    {
// Menugaskan variabel max untuk nilai z
        max = z; 
    }
// Mengembalikan nilai max 
return max;
}// Mengakhiri fungsi maximum()
