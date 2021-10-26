// Program menghitung nilai
#include <stdio.h>

int main()
{

    // Mendefinisikan variabel a, b, c, dan d dengan tipe data integer
    int a,b,c,d ;
  
    // Menginisialisasi variabel a, b, dan c
    a = 15;
    b = 4;
    c = 7;

    // Melakukan operasi aritmatika yang akan ditugaskan ke variabel d
    d = a % c + b;

    // Mencetak output
    printf("nilai a: %d \n", a );
    printf("nilai b: %d \n", b );
    printf("nilai c: %d \n", c );
    printf( "sisa hasil bagi dari a dibagi c kemudian ditambah b adalah %d", d );
    
    return 0;
}

