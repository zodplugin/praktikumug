#include <stdio.h>

int main()
{
  printf("Nama\t\tNilai\n");
  char *nilaiMhs[3][2] = 
  {
    {"Bella","A"},
    {"Siska","B"},
    {"Fajar","A"},
  };

  // Tampilkan nilai mahasiswa
  int i, j;
  for (i = 0; i < 3;i++) // Statement untuk iterasi baris (i)
  {
     for (j = 0; j < 2;j++ ){ // Statement untuk iterasi kolom (j)
        
        // Mencetak nilai dari variabel nilaiMhs
        printf("%s\t\t", nilaiMhs[i][j]);
     }

     printf("\n");
  }

  return 0;
  
}
