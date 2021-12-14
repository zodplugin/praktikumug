#include <stdio.h>
#include <string.h> 

int main()
{
  char *data_mhs[2][3][3]=
  {
    {{"Atika","Ferdi", "Budi"},
     {"Kayla", "Jesica", "Michael"},
     {"Andrean", "Karina", "Julian"}},
    {{"Layla","Farida", "Meily"},
     {"Firman", "Anita", "Gita"},
     {"Jonathan", "Lola", "Fikri"}}

  };
// Tampilkan data mahasiswa
  int i, j, k;
  printf ("Data peserta lolos seleksi asisten :\n");
  // Iterasi indeks kesatu (i)
  for (i = 0; i < 2; i++)
     // Iterasi indeks kedua (j)
     for (j = 0; j < 3 ; j++)
        // Iterasi indeks ketiga (k)
        for (k = 0; k < 3; k++)
        {
            // Kondisi ekspresi percabangan untuk menampilkan data Karina
            if (strcmp(data_mhs[i][j][k],"Karina") == 0){
                // Mencetak nama Karina jika kondisi terpenuhi
                printf("Hari ke-%d | Sesi ke-%d = %s\n", i+1,j+1,data_mhs[i][j][k]);
            }
        }

  return 0;
  
}
