#include <stdio.h>
// Masukkan library untuk memasukkan fungsi matematika
#include <math.h>

int main()
{
    // Mendeklarasikan variabel luasPermukaan, sisi, dan vKubus bertipe data float
    float luasPermukaan,sisi,vKubus;

  printf("Program mencari sisi dan volume kubus berdasarkan luas permukaan kubus\n");
  printf("\nMasukkan luas permukaan kubus: ");
  // Gunakan scanf untuk membaca input nilai untuk variabel luasPermukaan
  scanf("%f",&luasPermukaan);

  // Mencari nilai sisi dan vKubus
  // Menugaskan variabel sisi untuk menampung fungsi sqrt dari variabel luasPermukaan dibagi 6
  sisi = sqrt(luasPermukaan/6); // Digunakan untuk mencari nilai sisi
  // Menugaskan variabel vKubus untuk menampung fungsi pow dari variabel sisi
  vKubus = pow(sisi,3); // Digunakan untuk mencari volume kubus

  printf("\nJika diketahui luas permukaan kubus adalah %.2f, maka:\n", luasPermukaan);
  printf("1. Panjang sisi kubus adalah %.2f\n", sisi); // Mencetak nilai sisi
  printf("2. Dan volume kubusnya adalah %.2f", vKubus); // Mencetak nilai volume kubus

return 0;
}
