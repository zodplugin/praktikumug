#include <stdio.h>

int main()
{
  // Deklarasi variabel bil bertipe data integer
  int bil;

  printf("Masukkan angka: ");
  scanf("%d", &bil);// Membaca hasil input user dengan scanf

  // Memulai perulangan while dengan mendeklarasikan kondisi ekspresinya
  while (bil >= 0)
  {
      printf("%d\n",bil); // Mencetak nilai dari variabel bil

      bil -= 5; // Menugaskan variabel bil dengan hasil evaluasi bil - 5
  }

  return 0;
}
