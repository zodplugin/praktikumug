#include <stdio.h>

int main()
{
  int bil = 2 ; // Deklarasi dan inisialisasi variabel bil
  while (bil <= 16)  // Buat kondisi pada perulangan while bahwa bil <= 16
  {
    printf("%d\n",bil); // Mencetak nilai bil

    bil = bil + 2; // Statement increment bil + 2
  } 

  return 0;
}
