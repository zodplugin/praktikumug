#include <stdio.h>
int main()
{
    // Deklarasi variabel alphabet bertipe karakter
    char alphabet;

    /*
    Perulangan for dengan ekspresi pertama menugaskan variabel alphabet dengan A,
    ekspresi kedua menyeleksi kondisi variabel alphabet kurang dari K,
    ekspresi ketiga variabel alphabet increment
    */
    for (alphabet = 'A'; alphabet < 'K'; alphabet++)

  	    // Mencetak nilai variabel alphabet
  	    printf("%c ", alphabet);
  	
    return 0;
}
