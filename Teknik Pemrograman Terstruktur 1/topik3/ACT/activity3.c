#include <stdio.h>

int main()
{
    // Deklarasi variabel i dan j bertipe integer
    int i,j;
    
    // Menugaskan variabel i dengan 1
    i = 1;
    
    /* 
    Perulangan for pertama dengan ekspresi pertama menugaskan variabel i dengan 1,
    ekspresi kedua seleksi kondisi variabel i kurang dari sama dengan 5
    ekspresi ketiga variabel i increment
    */
    for(i=1 ; i <= 5; i++) 
        {
            /* 
            Perulangan for kedua dengan ekspresi pertama menugaskan variabel j dengan 1,
            ekspresi kedua seleksi kondisi variabel j kurang dari sama dengan variabel i
            ekspresi ketiga variabel j increment
            */
            for(j=1 ; j <= i; j++){
                // Mencetak simbol *
                printf("* ");
            }
            // Mencetak baris baru
            printf("\n");
        }

  return 0;
}
