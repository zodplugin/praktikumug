// Program square.c
#include <stdio.h>

// Fungsi prototype dengan nama fungsi square dan argument bertipe data integer
int square(int x);

// Fungsi main untuk memulai eksekusi program
int main()
{
    // Menugaskan variabel a bertipe data integer dengan nilai 10
    int a = 10;
    
    // Mencetak output dengan memanggil fungsi square
    printf("Persegi dengan sisi %d, luasnya adalah: %d\n", a, square(a));
    
    return 0;
} // Mengakhiri fungsi main()
    
// Mendefinisikan fungsi square
int square (int x)
{
    // Gunakan statement return x * x untuk mengembalikan nilai
    return x * x;    
} // Mengakhiri fungsi square()
