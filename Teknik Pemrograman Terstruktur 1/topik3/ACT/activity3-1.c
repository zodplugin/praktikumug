#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Deklarasi variabel a, b, dan c bertipe integer
    int a,b,c;

    // Menugaskan variabel a dengan sepuluh
    a = 10;

    /* 
    Statement for pertama menugaskan b dengan a,
    menyeleksi kondisi b lebih dari sama dengan satu,
    b decrement 
    */
    for(b=a; b >= 1;b--)
    {

        /* 
        Statement for kedua (nested for) menugaskan c dengan 1
        menyeleksi kondisi c kurang dari sama dengan b,
        c increment 
        */
        for (c=1; c<=b;c++){
            // Mencetak simbol asterik
            printf("*");
        }

    // Mencetak baris baru
    printf("\n");
    }

    return 0;
}
