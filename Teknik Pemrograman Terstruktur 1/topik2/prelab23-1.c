#include <stdio.h>
#include <stdbool.h>

int main()
{
    // Mendeklarasikan variabel hasil1 dan hasil2 dengan tipe data boolean pada satu baris
    bool hasil1, hasil2;

    printf("Hasil 1 merupakan benar (true) \ndan 0 merupakan salah (false)\n");

    hasil1 = 10 > 2; // Variabel hasil1 akan ditugaskan dengan hasil evaluasi ekspresi benar
    printf("Hasil1 10 > 2 = %d\n", hasil1 );

    hasil2 = -5 > 3; // Variabel hasil2 akan ditugaskan dengan hasil evaluasi ekspresi salah
    printf("Hasil2 -5 > 3 = %d\n", hasil2);

    return 0;
}
