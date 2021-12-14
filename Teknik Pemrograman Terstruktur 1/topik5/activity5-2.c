#include <stdio.h>

int main() {
  /* Deklarasi variabel array matriks1 dengan 2 baris dan 2 kolom, 
  matriks2 dengan 2 baris 1 kolom, dan hasil dengan 2 baris 1 kolom*/
  int matriks1[2][2], matriks2[2][1], hasil[2][1];
  // Deklarasi variabel i, j, k dan jumlah, serta menugaskan variabel jumlah dengan nilai 0
  int i, j, k, jumlah = 0;

    printf("Masukkan elemen matriks pertama: \n");
    // Iterasi untuk baris (i) pada matriks pertama
    for(i = 0; i < 2; i++){
      // Iterasi untuk kolom (j) pada matriks pertama
      for(j = 0; j < 2; j++){
        scanf("%d", &matriks1[i][j]);
      }
    }

    printf("Masukkan elemen matriks kedua: \n");
    // Iterasi untuk baris (i) pada matriks kedua
    for(i = 0; i < 2; i++){
      // Iterasi untuk kolom (j) pada matriks kedua
      for(j = 0; j < 1; j++){
        scanf("%d", &matriks2[i][j]);
      }
    }

    for(i = 0; i < 2; i++){ // Iterasi untuk mencetak baris matriks hasil
      for(j = 0; j < 1; j++){ // Iterasi untuk mencetak kolom matriks hasil
        for(k = 0; k < 2; k++){ // Iterasi untuk mencetak ada berapa matriks yang akan dicetak
          jumlah = jumlah + matriks1[i][k] * matriks2[k][j];
        }
        hasil[i][j] = jumlah;
        jumlah = 0;
      }
    }

    printf("Hasil perkalian matriks: \n");
    for(i = 0; i < 2; i++){
      for(j = 0; j < 1; j++){
        printf("%d", hasil[i][j]);
      }
      printf("\n");
    }


  return 0;
}
