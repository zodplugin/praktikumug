// Program persegi.c
#include <stdio.h>
#include <stdio.h>
// Fungsi prototype dengan nama fungsi persegi dan satu argument (y) bertipe data integer
int persegi(int y);

// Fungsi main untuk memulai eksekusi program
int main()
{
    // Membuat looping for dengan inisialisasi variabel x dengan nilai 1
    // dengan kondisi x lebih kecil sama dengan 10, dan increment x
    int x;
	for (x = 1; x <= 10;x++)
    {
        //Mencetak output dengan memanggil fungsi persegi
        printf("%d ", persegi(x));
    }
} // Mengakhiri fungsi main()
	
// Definisi fungsi persegi mengembalikan parameternya
int persegi(int y)
{
    // Menghitung luas persegi dan mengembalikan hasil
    int hasil = y * y;
    return hasil;
} // Mengakhiri fungsi persegi()
