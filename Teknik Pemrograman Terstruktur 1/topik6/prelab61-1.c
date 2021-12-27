// Program data_pegawai.c
#include <stdio.h>
#include <string.h>

int main()
{
    // Deklarasikan struct dengan nama struct pegawai
  struct pegawai
  {
      
      // Deklarasikan char fname dan lname dengan indeks 10, id bertipe integer dan gaji bertipe float
    char fname[10];
    char lname[10];
    int id;
    float gaji;
  };
  
  // Deklarasikan variabel struct dengan nama pgw
  struct pegawai pgw;
  
  // Menugaskan anggota struct fname dan lname dengan Michael dan Budi dengan menggunakan fungsi string copy
  strcpy(pgw.fname,"Michael");
  strcpy(pgw.lname, "Budi");
  
  // Menugaskan anggota struct id dengan nilai 1234 dan anggota struct gaji dengan 1000000.00
  pgw.id = 1234;
  pgw.gaji = 1000000.00;
  

  // Mencetak nilai anggota struct fname, lname, id, dan gaji
  printf("Nama depan: %s\n", pgw.fname);
  printf("Nama belakang: %s\n", pgw.lname);
  printf("ID Pegawai: %d\n", pgw.id);
  printf("Gaji : Rp.%.2f\n", pgw.gaji);
  return 0;
  
}
