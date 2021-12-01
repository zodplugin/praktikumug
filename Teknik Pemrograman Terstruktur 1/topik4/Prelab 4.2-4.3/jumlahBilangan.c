// Program jumlahBilangan.c
#include <stdio.h>

// Buat fungsi prototype jumlahDigit bertipe data integer
int jumlahDigit(int);

// Function jumlahDigit untuk menghitung jumlah digit angka bilangan
int jumlahDigit(int x)
{
  // Statement if dengan kondisi variabel bilangan sama dengan 0
 if (x == 0){
     return 0;
 }
  // Mengembalikan nilai dari hasil evaluasi sisa bagi dari
  // variabel bilangan dengan 10 di jumlahkan dengan hasil evaluasi
  // variabel bilangan dengan 10 dalam function jumlahDigit
  
  return ( x %10) + jumlahDigit(x/10);
}

// Function main untuk memulai eksekusi program
int main()
{
  // Deklarasi variabel bilangan dan hasil yang bertipe data integer
  int bilangan, hasil;
  
  // Mencetak output dan memasukkan nilai pada variabel bilangan
  printf("Masukkan angka bilangan bulat: \n");
  scanf("%d", &bilangan);
  
  // Menugaskan nilai pada variabel bilangan pada function jumlahDigit ke
  // variabel hasil
  hasil = jumlahDigit(bilangan);
  
  // Mencetak output dan memanggil variabel hasil
  printf("Jumlah digit angka bilangan: %d\n", hasil);

  
  return 0;
}
