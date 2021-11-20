#include <stdio.h>

int main()
{
  // Deklarasi variabel bil, jumlah, dan angka bertipe data integer
  int bil,jumlah,angka ;

  printf("Masukkan angka: ");
  scanf("%d", &angka);

  // Menugaskan variabel jumlah dengan nilai 0
  jumlah = 0 ;

  // Menugaskan variabel bil dengan nilai 1
  bil = 1 ;

  // Memulai perulangan do
  do
  {
      // Menginisialisasikan variabel jumlah untuk ditugaskan dengan ekspresi jumlah + bil
      jumlah = jumlah + bil ;

      // Gunakan post-increment pada variabel bil
      bil++ ;
  }while(bil <= angka); // Gunakan keyword while dengan kondisi bil <= angka

  printf("Jumlah = %d\n", jumlah);

  return 0;
}
